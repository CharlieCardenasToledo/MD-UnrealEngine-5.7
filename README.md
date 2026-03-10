# Epic Docs Scraper & Offline Guide

Este proyecto te permite descargar la documentación oficial de Unreal Engine desde Epic Games y compilarla en diferentes formatos (archivos individuales, una guía completa de texto, o un sitio web navegable).

Está diseñado explícitamente para que cualquier desarrollador pueda buscar, leer y navegar por la inmensa documentación de Unreal Engine de manera offline, rápida y cómoda.

---

## 📖 Navegación Fácil y Profesional (Recomendado)

La forma más potente y sencilla de leer la documentación generada es utilizando **MkDocs Material**. Esto te crea un sitio web local con un buscador instantáneo, menú lateral jerárquico y un diseño limpio.

### Instrucciones rápidas:

1. Asegúrate de tener Python instalado y las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Genera el archivo de navegación (`mkdocs.yml`):
   ```bash
   python scripts/build_guide.py --mode mkdocs --docs-dir docs-md-py
   ```
3. Levanta el servidor local:
   ```bash
   mkdocs serve
   ```
4. Abre `http://127.0.0.1:8000` en tu navegador. Tendrás acceso inmediato a toda la documentación de Unreal Engine con búsqueda en tiempo real y árbol de navegación completo.

---

## 🗂️ Otros Formatos de Lectura

Si prefieres no utilizar un servidor local, el script generador (`build_guide.py`) puede compilar otros formatos útiles:

### Índice Jerárquico en Markdown

Genera un `GUIDE_INDEX.md` en la raíz del proyecto. Este archivo contiene enlaces relativos a todos los archivos `.md` locales organizados en niveles (1., 1.1., 1.2.2., etc.).

```bash
python scripts/build_guide.py --mode index --docs-dir docs-md-py
```

_Abre el archivo `GUIDE_INDEX.md` en tu editor de código o visor de Markdown preferido (por ejemplo, VS Code o Obsidian)._

### Libro Completo (Un solo archivo)

Genera un único archivo gigante (`GUIDE_BOOK.md` - ~30 MB) con **toda** la documentación concatenada en orden. Ideal si quieres buscar texto libre `Ctrl+F` a través de toda la base de conocimiento sin cambiar de archivo, o si quieres usarlo como corpus de texto para IAs locales o procesos de RAG.

```bash
python scripts/build_guide.py --mode book --docs-dir docs-md-py
```

---

## ⚙️ Actualizar la Documentación (Scraping)

El proyecto incluye un scraper inteligente a prueba de interrupciones (`scrape_epic_docs.py`).

### Características:

- **Descarga multihilo**: Soporta N _workers_ concurrentes para máxima velocidad (`--workers N`).
- **Caché Inteligente**: Por defecto, salta los archivos que ya se han descargado (`--skip-existing`). Puedes pausar y reanudar el script cuando quieras.
- **Jerarquía preservada**: Descarga la tabla de contenidos oficial y preserva la estructura a través de un archivo maestro `toc-tree.json`.

### Cómo ejecutar o actualizar:

1. Ejecuta el scraper (por defecto usa 1 worker, recomendamos 4 o más para equipos potentes):
   ```bash
   python scripts/scrape_epic_docs.py --out-dir docs-md-py --workers 4
   ```
2. _(Opcional)_ Si hubo errores (ej: caídas de red), el script generará un log. Si quieres forzar regeneración:
   ```bash
   python scripts/scrape_epic_docs.py --out-dir docs-md-py --force
   ```

---

## 🗃️ Estructura del Repositorio

- `scripts/scrape_epic_docs.py`: Motor de recolección y web-scraping iterativo.
- `scripts/build_guide.py`: Compilador de índices, libros unificados y configuración de interfaz web.
- `docs-md-py/`: Carpeta (directorio objetivo) donde se almacenan todos los Markdown descargados y estructurados.
- `GUIDE_INDEX.md` / `GUIDE_BOOK.md`: Productos generados por el builder.
- `mkdocs.yml`: Archivo base generado automáticamente para el servidor de visualización.

---

_Nota: Todo el contenido descargado es propiedad de Epic Games. Esta herramienta es exclusivamente un lector offline de documentación pública para uso personal o interno de estudio._
