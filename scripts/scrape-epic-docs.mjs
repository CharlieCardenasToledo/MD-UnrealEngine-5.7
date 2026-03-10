import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { load } from "cheerio";
import TurndownService from "turndown";

const START_URL =
  process.argv[2] ??
  "https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-the-basics-of-unreal-engine";
const MAX_PAGES = Number(process.argv[3] ?? 500);
const OUT_DIR = process.argv[4] ?? "docs-md";
const CRAWL_DELAY_MS = Number(process.argv[5] ?? 250);

const parsedStart = new URL(START_URL);
const ALLOWED_HOST = parsedStart.host;
const ALLOWED_PATH_PREFIX = "/documentation/en-us/unreal-engine/";

const turndown = new TurndownService({
  headingStyle: "atx",
  codeBlockStyle: "fenced",
  emDelimiter: "_",
});

turndown.keep(["table", "thead", "tbody", "tr", "th", "td"]);

function isAllowedUrl(url) {
  return (
    url.host === ALLOWED_HOST &&
    url.pathname.startsWith(ALLOWED_PATH_PREFIX) &&
    !url.pathname.includes("/api/") &&
    !url.pathname.endsWith(".json")
  );
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function sanitizeSegment(segment) {
  return segment
    .trim()
    .replace(/[^a-zA-Z0-9-_]/g, "-")
    .replace(/-+/g, "-")
    .replace(/^-|-$/g, "")
    .toLowerCase();
}

function filePathForUrl(url) {
  const segments = url.pathname
    .split("/")
    .filter(Boolean)
    .map((s) => sanitizeSegment(s));
  const last = segments.length ? segments[segments.length - 1] : "index";
  return path.join(...segments.slice(0, -1), `${last}.md`);
}

function pickContentRoot($) {
  const selectors = [
    "main article",
    "article",
    "main",
    "[role='main']",
    ".documentation-page",
    ".content",
  ];
  for (const selector of selectors) {
    const node = $(selector).first();
    if (node.length) return node;
  }
  return $("body").first();
}

function cleanupDom($, root) {
  root
    .find(
      "script,style,noscript,svg,button,header,footer,nav,.breadcrumbs,.toc,.sidebar,.feedback,form,iframe"
    )
    .remove();
}

async function ensureDir(p) {
  await fs.mkdir(p, { recursive: true });
}

async function writeMarkdown(baseDir, url, markdown) {
  const relativeFile = filePathForUrl(url);
  const absFile = path.join(baseDir, relativeFile);
  await ensureDir(path.dirname(absFile));
  await fs.writeFile(absFile, markdown, "utf8");
  return relativeFile;
}

async function fetchHtml(url) {
  const response = await fetch(url, {
    headers: {
      "user-agent":
        "Mozilla/5.0 (compatible; UnrealDocsScraper/1.0; +https://dev.epicgames.com/)",
    },
  });

  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`);
  }

  return response.text();
}

function makeMarkdown(url, title, bodyMd) {
  return `# ${title}\n\n> Source: ${url}\n\n${bodyMd}\n`;
}

async function run() {
  const visited = new Set();
  const queued = new Set([START_URL]);
  const queue = [START_URL];
  const outAbs = path.resolve(OUT_DIR);
  const written = [];
  const failures = [];

  await ensureDir(outAbs);

  while (queue.length && visited.size < MAX_PAGES) {
    const current = queue.shift();
    queued.delete(current);
    if (!current || visited.has(current)) continue;
    visited.add(current);

    const currentUrl = new URL(current);
    if (!isAllowedUrl(currentUrl)) continue;

    process.stdout.write(
      `[${visited.size}/${MAX_PAGES}] Fetching ${currentUrl.toString()}\n`
    );

    try {
      const html = await fetchHtml(currentUrl.toString());
      const $ = load(html);
      const root = pickContentRoot($).clone();
      cleanupDom($, root);

      root.find("a").each((_, a) => {
        const href = $(a).attr("href");
        if (!href) return;
        try {
          const nextUrl = new URL(href, currentUrl);
          nextUrl.hash = "";
          if (!isAllowedUrl(nextUrl)) return;
          const next = nextUrl.toString();
          if (!visited.has(next) && !queued.has(next)) {
            queue.push(next);
            queued.add(next);
          }
        } catch {
          // Ignore malformed links.
        }
      });

      const title =
        $("h1").first().text().trim() ||
        $("title").text().trim() ||
        currentUrl.pathname.split("/").filter(Boolean).pop() ||
        "Untitled";
      const bodyHtml = root.html() ?? "";
      const bodyMd = turndown.turndown(bodyHtml).trim();
      const finalMd = makeMarkdown(currentUrl.toString(), title, bodyMd);
      const relativeFile = await writeMarkdown(outAbs, currentUrl, finalMd);
      written.push({ url: currentUrl.toString(), file: relativeFile, title });
    } catch (error) {
      failures.push({ url: currentUrl.toString(), error: String(error) });
    }

    if (CRAWL_DELAY_MS > 0) {
      await sleep(CRAWL_DELAY_MS);
    }
  }

  const indexLines = [
    "# Unreal Engine Docs (Scraped)",
    "",
    `- Start URL: ${START_URL}`,
    `- Generated at: ${new Date().toISOString()}`,
    `- Total pages: ${written.length}`,
    `- Failures: ${failures.length}`,
    "",
    "## Pages",
    "",
    ...written.map((x) => `- [${x.title}](${x.file.replace(/\\/g, "/")})`),
  ];
  await fs.writeFile(path.join(outAbs, "INDEX.md"), indexLines.join("\n"), "utf8");

  if (failures.length) {
    const failureLines = [
      "# Failures",
      "",
      ...failures.map((f) => `- ${f.url}: ${f.error}`),
      "",
    ];
    await fs.writeFile(
      path.join(outAbs, "FAILURES.md"),
      failureLines.join("\n"),
      "utf8"
    );
  }

  process.stdout.write(
    `Done. Wrote ${written.length} files to ${outAbs}. Failures: ${failures.length}\n`
  );
}

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
if (__dirname) {
  run().catch((err) => {
    console.error(err);
    process.exit(1);
  });
}
