import argparse
import json
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import cloudscraper
from markdownify import markdownify as md


BASE_DOC_URL = "https://dev.epicgames.com/documentation"
BASE_API_URL = "https://dev.epicgames.com/community/api/documentation"


# ---------------------------------------------------------------------------
# Text / HTML helpers
# ---------------------------------------------------------------------------

def normalize_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("\xa0", " ")).strip()


def html_to_markdown(html: Optional[str]) -> str:
    if not html:
        return ""
    out = md(html, heading_style="ATX")
    return out.strip()


def is_hidden(block: Dict[str, Any]) -> bool:
    return bool((block.get("settings") or {}).get("is_hidden"))


def make_image_url(block: Dict[str, Any]) -> str:
    storage_key = block.get("storage_key") or (block.get("image") or {}).get("storage_key")
    context = block.get("context") or (block.get("image") or {}).get("context") or "documentation"
    if not storage_key:
        return ""
    return f"https://dev.epicgames.com/community/api/{context}/image/{storage_key}"


def build_local_doc_link(doc_hash_id: str, hash_to_path: Dict[str, str]) -> str:
    target = hash_to_path.get(doc_hash_id)
    return target or ""


# ---------------------------------------------------------------------------
# Block → Markdown
# ---------------------------------------------------------------------------

def inline_from_blocks(
    blocks: Iterable[Dict[str, Any]], hash_to_path: Dict[str, str]
) -> str:
    parts: List[str] = []
    for b in blocks:
        t = b.get("type")
        if t in {"paragraph", "header", "enhanced_table_header"}:
            txt = html_to_markdown(b.get("content") or b.get("content_html") or "")
            if txt:
                parts.append(normalize_ws(txt))
        elif t == "markdown":
            txt = html_to_markdown(b.get("content_html") or b.get("content") or "")
            if txt:
                parts.append(normalize_ws(txt))
        elif t == "image":
            img = make_image_url(b)
            alt = normalize_ws(b.get("alt_text") or b.get("caption") or "Image")
            if img:
                parts.append(f"![{alt}]({img})")
        elif t == "video":
            identifier = (b.get("video") or {}).get("identifier") or b.get("video_id") or ""
            if identifier:
                parts.append(
                    f"[Video: {identifier}](https://dev.epicgames.com/community/api/cms/videos/{identifier}/embed.html)"
                )
        elif t == "document_list":
            doc_hash = b.get("document_hash_id")
            title = b.get("title") or "Related Document"
            if doc_hash:
                link = build_local_doc_link(doc_hash, hash_to_path)
                parts.append(f"[{title}]({link})" if link else f"[{title}]")
        elif t == "enhanced_list":
            # Flatten nested list in inline contexts.
            list_items = b.get("items") or []
            for item in list_items:
                if isinstance(item, list):
                    text = inline_from_blocks(item, hash_to_path)
                    if text:
                        parts.append(text)
    return normalize_ws(" ".join(parts))


def table_to_markdown(rows: List[Any], hash_to_path: Dict[str, str]) -> str:
    if not rows:
        return ""
    rendered: List[List[str]] = []
    for row in rows:
        cells = row or []
        rendered_row: List[str] = []
        for cell in cells:
            text = inline_from_blocks(cell or [], hash_to_path)
            rendered_row.append(text.replace("\n", "<br>").strip() or " ")
        rendered.append(rendered_row)
    if not rendered:
        return ""
    width = max(len(r) for r in rendered)
    rendered = [r + ([" "] * (width - len(r))) for r in rendered]
    header = rendered[0]
    sep = ["---"] * width
    body = rendered[1:] if len(rendered) > 1 else []
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(sep) + " |",
    ]
    for r in body:
        lines.append("| " + " | ".join(r) + " |")
    return "\n".join(lines)


def block_to_markdown(block: Dict[str, Any], hash_to_path: Dict[str, str]) -> str:
    if is_hidden(block):
        return ""
    btype = block.get("type")
    if btype == "header":
        level = int(block.get("level") or 2)
        level = max(1, min(level, 6))
        text = html_to_markdown(block.get("content") or "")
        return f'{"#" * level} {normalize_ws(text)}'.strip()
    if btype == "paragraph":
        return html_to_markdown(block.get("content") or "")
    if btype == "markdown":
        return html_to_markdown(block.get("content_html") or block.get("content") or "")
    if btype == "image":
        image_url = make_image_url(block)
        alt = normalize_ws(block.get("alt_text") or "Image")
        caption = normalize_ws(block.get("caption") or "")
        out = f"![{alt}]({image_url})" if image_url else f"![{alt}]()"
        if caption:
            out += f"\n\n_{caption}_"
        return out
    if btype == "video":
        identifier = (block.get("video") or {}).get("identifier") or block.get("video_id") or ""
        if not identifier:
            return ""
        url = f"https://dev.epicgames.com/community/api/cms/videos/{identifier}/embed.html"
        return f"[Video: {identifier}]({url})"
    if btype == "enhanced_list":
        style = block.get("style") or "unordered"
        list_lines: List[str] = []
        items = block.get("items") or []
        for idx, item in enumerate(items, start=1):
            text = inline_from_blocks(item or [], hash_to_path)
            if not text:
                continue
            prefix = f"{idx}. " if style == "ordered" else "- "
            list_lines.append(prefix + text)
        return "\n".join(list_lines)
    if btype == "document_list":
        doc_hash = block.get("document_hash_id")
        if doc_hash:
            target = build_local_doc_link(doc_hash, hash_to_path)
            doc_title = block.get("title") or "Related Document"
            if target:
                return f"- [{doc_title}]({target})"
            return f"- {doc_title}"
        doc_lines: List[str] = []
        for item in block.get("items") or []:
            if isinstance(item, dict):
                title = item.get("title") or "Document"
                item_hash = item.get("document_hash_id")
                target = build_local_doc_link(item_hash, hash_to_path) if item_hash else ""
                doc_lines.append(f"- [{title}]({target})" if target else f"- {title}")
        return "\n".join(doc_lines)
    if btype == "enhanced_table":
        return table_to_markdown(block.get("rows") or [], hash_to_path)
    if btype == "enhanced_table_header":
        return normalize_ws(html_to_markdown(block.get("content") or ""))
    # Fallback for unknown types.
    if "content" in block:
        return html_to_markdown(block.get("content") or "")
    if "content_html" in block:
        return html_to_markdown(block.get("content_html") or "")
    return f"```json\n{json.dumps(block, ensure_ascii=False, indent=2)}\n```"


# ---------------------------------------------------------------------------
# ToC helpers
# ---------------------------------------------------------------------------

def collect_entries(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Flatten the ToC tree into an ordered list (DFS, preserving order)."""
    out: List[Dict[str, Any]] = []

    def walk(nodes: List[Dict[str, Any]]) -> None:
        for e in nodes or []:
            out.append(e)
            walk(e.get("sub_entries") or [])

    walk(entries)
    return out


def safe_file_segment(seg: str) -> str:
    seg = seg.strip().lower()
    seg = re.sub(r"[^a-z0-9._-]+", "-", seg)
    seg = re.sub(r"-{2,}", "-", seg).strip("-")
    return seg or "untitled"


# ---------------------------------------------------------------------------
# File I/O
# ---------------------------------------------------------------------------

def write_markdown_file(out_dir: Path, rel_path: str, content: str) -> None:
    dest = out_dir / rel_path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content, encoding="utf-8")


def parse_failures_markdown(path: Path) -> List[str]:
    if not path.exists():
        return []
    routes: List[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^- `([^`]+)`: ", line.strip())
        if m:
            routes.append(m.group(1))
    return routes


# ---------------------------------------------------------------------------
# Network
# ---------------------------------------------------------------------------

def fetch_document_with_retries(
    scraper: Any,
    page_path: str,
    app_version: str,
    retries: int,
    retry_backoff: float,
) -> Tuple[Optional[Dict[str, Any]], Optional[str], int]:
    attempts = 0
    while True:
        attempts += 1
        try:
            params = {"path": page_path}
            if app_version:
                params["application_version"] = app_version
            resp = scraper.get(f"{BASE_API_URL}/document.json", params=params, timeout=90)
            if resp.status_code == 200:
                return resp.json(), None, attempts
            # 404 usually means removed/invalid slug; avoid wasting retries.
            if resp.status_code == 404:
                return None, "HTTP 404", attempts
            # Retry for temporary errors.
            if attempts <= retries:
                time.sleep(max(0.0, retry_backoff) * attempts)
                continue
            return None, f"HTTP {resp.status_code}", attempts
        except Exception as exc:
            if attempts <= retries:
                time.sleep(max(0.0, retry_backoff) * attempts)
                continue
            return None, str(exc), attempts


# ---------------------------------------------------------------------------
# Per-page processing (used by both serial and concurrent paths)
# ---------------------------------------------------------------------------

def process_entry(
    *,
    scraper: Any,
    entry: Dict[str, Any],
    locale: str,
    app_slug: str,
    app_version: str,
    out_dir: Path,
    hash_to_relpath: Dict[str, str],
    retries: int,
    retry_backoff: float,
    skip_existing: bool,
) -> Tuple[bool, Optional[Tuple[str, str, str]], Optional[Dict[str, Any]]]:
    """
    Returns (success, success_tuple, failure_dict).
    success_tuple = (title, source_url, rel_file)
    """
    slug = entry.get("slug") or ""
    if not slug:
        return False, None, None

    page_path = entry.get("page_path") or f"{locale}/{app_slug}/{slug}"
    parts = [p for p in page_path.strip("/").split("/") if p]
    if len(parts) >= 3:
        rel_file = (
            f"{safe_file_segment(parts[0])}/{safe_file_segment(parts[1])}/"
            f"{safe_file_segment(parts[-1])}.md"
        )
    else:
        rel_file = (
            f"{safe_file_segment(locale)}/{safe_file_segment(app_slug)}/"
            f"{safe_file_segment(slug)}.md"
        )

    dest = out_dir / rel_file
    if skip_existing and dest.exists():
        # Read title from existing file for the index
        first_line = dest.read_text(encoding="utf-8").splitlines()[0] if dest.exists() else ""
        title = first_line.lstrip("# ").strip() if first_line.startswith("#") else slug
        source_url = f"{BASE_DOC_URL}/{page_path}"
        return True, (title, source_url, rel_file), None

    doc, err, attempts = fetch_document_with_retries(
        scraper=scraper,
        page_path=page_path,
        app_version=app_version,
        retries=max(0, retries),
        retry_backoff=retry_backoff,
    )

    if doc is None:
        return False, None, {"path": page_path, "error": err or "Unknown error", "attempts": attempts}

    title = normalize_ws(doc.get("title") or entry.get("title") or slug)
    blocks = doc.get("blocks") or []
    rendered_blocks = [block_to_markdown(block, hash_to_relpath) for block in blocks]
    body = "\n\n".join([b for b in rendered_blocks if b and b.strip()])
    source_url = f"{BASE_DOC_URL}/{page_path}"
    md_content = (
        f"# {title}\n\n"
        f"> Source: {source_url}\n\n"
        f"> Application Version: {app_version or 'default'}\n\n"
        f"{body}\n"
    )
    write_markdown_file(out_dir, rel_file, md_content)
    return True, (title, source_url, rel_file), None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scrape Unreal Engine docs from dev.epicgames.com to Markdown files."
    )
    parser.add_argument(
        "--start-path",
        default="en-us/unreal-engine/understanding-the-basics-of-unreal-engine",
        help="Path in format locale/application/slug",
    )
    parser.add_argument("--application-version", default="")
    parser.add_argument("--out-dir", default="docs-md")
    parser.add_argument("--max-pages", type=int, default=0, help="0 = all")
    parser.add_argument("--delay", type=float, default=0.08,
                        help="Seconds to sleep between requests (only in serial mode)")
    parser.add_argument("--retries", type=int, default=2, help="Retries per page")
    parser.add_argument(
        "--retry-backoff", type=float, default=1.25, help="Seconds multiplier between retries"
    )
    parser.add_argument(
        "--pending-json",
        default="pending-routes.json",
        help="File name for pending routes report inside out-dir",
    )
    parser.add_argument(
        "--retry-failures-from",
        default="",
        help="Path to FAILURES.md to retry only pending routes (incremental mode)",
    )
    # New flags
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        default=True,
        help="Skip pages that already have a local .md file (default: True)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        default=False,
        help="Overwrite existing .md files (disables --skip-existing)",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        help="Number of parallel download workers (default: 1 = serial). "
             "Use 4-8 for faster scraping; be respectful with rate limiting.",
    )
    parser.add_argument(
        "--save-toc",
        action="store_true",
        default=True,
        help="Save the full hierarchical ToC tree to toc-tree.json (default: True)",
    )
    args = parser.parse_args()

    skip_existing = args.skip_existing and not args.force

    start_parts = [p for p in args.start_path.strip("/").split("/") if p]
    if len(start_parts) < 3:
        raise ValueError("start-path must look like: en-us/unreal-engine/some-page")
    locale, app_slug = start_parts[0], start_parts[1]

    scraper = cloudscraper.create_scraper(
        browser={"browser": "chrome", "platform": "windows", "mobile": False}
    )
    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    toc_params: Dict[str, str] = {"path": args.start_path}
    if args.application_version:
        toc_params["application_version"] = args.application_version

    print("Fetching Table of Contents...")
    toc_resp = scraper.get(
        f"{BASE_API_URL}/table_of_content.json", params=toc_params, timeout=90
    )
    toc_resp.raise_for_status()
    toc = toc_resp.json()

    app_version = args.application_version or (toc.get("all_versions") or [""])[0]
    retry_mode = bool(args.retry_failures_from)

    # Save the full hierarchical ToC tree for build_guide.py
    if args.save_toc and not retry_mode:
        toc_tree_path = out_dir / "toc-tree.json"
        toc_tree_path.write_text(
            json.dumps(
                {
                    "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                    "start_path": args.start_path,
                    "application_version": app_version,
                    "entries": toc.get("entries") or [],
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        print(f"ToC tree saved to {toc_tree_path}")

    entries = collect_entries(toc.get("entries") or [])

    if retry_mode:
        retry_path = Path(args.retry_failures_from)
        retry_routes = parse_failures_markdown(retry_path)
        # In retry mode we rebuild the full hash map from the original ToC tree
        # so that internal document links work correctly.
        all_entries_for_hash = collect_entries(toc.get("entries") or [])
        entries = [{
            "slug": r.split("/")[-1],
            "page_path": r,
            # Preserve document_hash_id if available from original ToC
            "document_hash_id": next(
                (e.get("document_hash_id") for e in all_entries_for_hash
                 if e.get("page_path") == r or e.get("slug") == r.split("/")[-1]),
                None,
            ),
        } for r in retry_routes]
        print(f"Retry mode enabled. Routes loaded from {retry_path}: {len(entries)}")
    elif args.max_pages > 0:
        entries = entries[: args.max_pages]

    # Build hash → relative path map using the full ToC (not just retry subset)
    hash_source = collect_entries(toc.get("entries") or [])
    hash_to_relpath: Dict[str, str] = {}
    for e in hash_source:
        slug = safe_file_segment(e.get("slug") or "")
        page_path = e.get("page_path") or f"{locale}/{app_slug}/{slug}"
        parts = [p for p in page_path.strip("/").split("/") if p]
        if len(parts) >= 3:
            rel = (
                f"{safe_file_segment(parts[0])}/{safe_file_segment(parts[1])}/"
                f"{safe_file_segment(parts[-1])}.md"
            )
        else:
            rel = f"{safe_file_segment(locale)}/{safe_file_segment(app_slug)}/{slug}.md"
        if e.get("document_hash_id"):
            hash_to_relpath[e["document_hash_id"]] = rel

    successes: List[Tuple[str, str, str]] = []
    failures: List[Dict[str, Any]] = []

    total = len(entries)
    workers = max(1, args.workers)
    print(f"Processing {total} pages with {workers} worker(s). skip_existing={skip_existing}")

    if workers == 1:
        # Serial path (original behavior + skip_existing)
        for idx, entry in enumerate(entries, start=1):
            slug = entry.get("slug") or ""
            page_path = entry.get("page_path") or f"{locale}/{app_slug}/{slug}"
            try:
                ok, success_tuple, fail_dict = process_entry(
                    scraper=scraper,
                    entry=entry,
                    locale=locale,
                    app_slug=app_slug,
                    app_version=app_version,
                    out_dir=out_dir,
                    hash_to_relpath=hash_to_relpath,
                    retries=args.retries,
                    retry_backoff=args.retry_backoff,
                    skip_existing=skip_existing,
                )
                if ok and success_tuple:
                    successes.append(success_tuple)
                    label = "SKIP" if skip_existing and (out_dir / success_tuple[2]).exists() else "OK  "
                    print(f"[{idx}/{total}] {label} {page_path}")
                elif fail_dict:
                    failures.append(fail_dict)
                    print(f"[{idx}/{total}] FAIL {page_path}: {fail_dict['error']} (attempts={fail_dict['attempts']})")
            except Exception as exc:
                failures.append({"path": page_path, "error": str(exc), "attempts": 1})
                print(f"[{idx}/{total}] FAIL {page_path}: {exc}")
            if args.delay > 0:
                time.sleep(args.delay)
    else:
        # Concurrent path
        # We need per-thread scrapers — cloudscraper is not thread-safe
        def make_scraper() -> Any:
            return cloudscraper.create_scraper(
                browser={"browser": "chrome", "platform": "windows", "mobile": False}
            )

        import threading
        _local = threading.local()

        def get_scraper() -> Any:
            if not hasattr(_local, "scraper"):
                _local.scraper = make_scraper()
            return _local.scraper

        def worker_fn(idx: int, entry: Dict[str, Any]) -> Tuple[int, bool, Any, Any]:
            _scraper = get_scraper()
            page_path = entry.get("page_path") or ""
            try:
                ok, success_tuple, fail_dict = process_entry(
                    scraper=_scraper,
                    entry=entry,
                    locale=locale,
                    app_slug=app_slug,
                    app_version=app_version,
                    out_dir=out_dir,
                    hash_to_relpath=hash_to_relpath,
                    retries=args.retries,
                    retry_backoff=args.retry_backoff,
                    skip_existing=skip_existing,
                )
                return idx, ok, success_tuple, fail_dict
            except Exception as exc:
                return idx, False, None, {"path": page_path, "error": str(exc), "attempts": 1}

        with ThreadPoolExecutor(max_workers=workers) as executor:
            future_map = {
                executor.submit(worker_fn, idx, entry): (idx, entry)
                for idx, entry in enumerate(entries, start=1)
            }
            for future in as_completed(future_map):
                idx, entry = future_map[future]
                page_path = entry.get("page_path") or entry.get("slug") or ""
                try:
                    _idx, ok, success_tuple, fail_dict = future.result()
                    if ok and success_tuple:
                        successes.append(success_tuple)
                        print(f"[{_idx}/{total}] OK   {page_path}")
                    elif fail_dict:
                        failures.append(fail_dict)
                        print(f"[{_idx}/{total}] FAIL {page_path}: {fail_dict['error']}")
                except Exception as exc:
                    failures.append({"path": page_path, "error": str(exc), "attempts": 1})
                    print(f"[{idx}/{total}] FAIL {page_path}: {exc}")

    # Reports
    if not retry_mode:
        index_lines: List[str] = [
            "# Unreal Engine Docs Export",
            "",
            f"- Start path: `{args.start_path}`",
            f"- Application version: `{app_version}`",
            f"- Pages exported: `{len(successes)}`",
            f"- Failures: `{len(failures)}`",
            "",
            "## Pages",
            "",
        ]
        for title, _, rel_file in successes:
            index_lines.append(f"- [{title}]({rel_file.replace(chr(92), '/')})")
        (out_dir / "INDEX.md").write_text("\n".join(index_lines), encoding="utf-8")
    else:
        retry_lines = [
            "# Incremental Retry Report",
            "",
            f"- Source failures file: `{args.retry_failures_from}`",
            f"- Application version: `{app_version}`",
            f"- Recovered in this run: `{len(successes)}`",
            f"- Still pending: `{len(failures)}`",
            "",
        ]
        if successes:
            retry_lines.append("## Recovered")
            retry_lines.append("")
            for title, _, rel_file in successes:
                retry_lines.append(f"- [{title}]({rel_file.replace(chr(92), '/')})")
            retry_lines.append("")
        (out_dir / "RETRY-REPORT.md").write_text("\n".join(retry_lines), encoding="utf-8")

    pending_path = out_dir / args.pending_json
    pending_payload = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "mode": "retry" if retry_mode else "full",
        "start_path": args.start_path,
        "application_version": app_version,
        "total_entries": total,
        "exported": len(successes),
        "pending_count": len(failures),
        "pending": failures,
    }
    pending_path.write_text(
        json.dumps(pending_payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    if failures:
        fail_lines = ["# Failures", ""]
        for f in failures:
            fail_lines.append(
                f"- `{f['path']}`: {f['error']} (attempts={f.get('attempts', '?')})"
            )
        (out_dir / "FAILURES.md").write_text("\n".join(fail_lines), encoding="utf-8")
    else:
        try:
            (out_dir / "FAILURES.md").unlink()
        except FileNotFoundError:
            pass

    print(
        f"Done. Exported {len(successes)} pages to {out_dir}. "
        f"Failures: {len(failures)}. Pending report: {pending_path}"
    )


if __name__ == "__main__":
    main()
