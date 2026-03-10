# 🤖 Integración con Inteligencia Artificial (LLMs)

El gran valor de tener la documentación entera de Unreal Engine en formato **Markdown estructurado** es que es el formato nativo preferido por los Modelos de Lenguaje Grandes (LLMs).

A diferencia del HTML lleno de ruido web o PDFs pesados, el Markdown generado en este proyecto es 100% texto limpio. Aquí tienes las mejores estrategias para usar estos datos con **cualquier LLM** (ChatGPT, Claude, Gemini, Llama, etc.).

---

## 1. Asistentes de Código (Cursor, GitHub Copilot, Cline)

La forma más directa de usar esta documentación para programar.

**Cómo hacerlo:**

1. Abre tu proyecto de Unreal Engine en un editor con IA (como Cursor).
2. Agrega la carpeta `docs-md-py` al _Workspace_ secundario del editor, o utiliza la función de indexación local (ej. `@Codebase` o `@Folders` en Cursor).
3. La IA indizará automáticamente los miles de archivos `.md` y los usará como contexto altamente preciso cuando le preguntes _"¿Cómo implemento X en C++ para Unreal Engine 5.7?"_.

## 2. Bases de Conocimiento sin Código (NotebookLM, Custom GPTs, Claude Projects)

Ideal si no quieres programar tu propia IA pero quieres un "Experto en Unreal Engine" personal.

**Cómo hacerlo:**

- **Google NotebookLM / Custom GPTs (OpenAI) / Projects (Anthropic)**: Estas plataformas permiten subir archivos para crear una base de conocimiento aislada (RAG automático).
- **El reto del tamaño**: El archivo `GUIDE_BOOK.md` pesa ~30MB (aprox. 7-8 millones de tokens). La mayoría de los LLMs comerciales tienen un límite de contexto de 128K a 200K tokens (Gemini 1.5 Pro llega a 2M).
- **La solución**: Comprime la carpeta `docs-md-py` entera en un archivo `.zip` y súbela a tu Custom GPT o Claude Project. Las plataformas modernas extraerán el ZIP, leerán los Markdowns y buscarán en ellos cuando les hagas una pregunta.

## 3. Construir tu propio RAG (Retrieval-Augmented Generation)

Si estás desarrollando tu propia aplicación o script de IA (usando LangChain, LlamaIndex, o llamadas directas a APIs), la estructura individual de la carpeta `docs-md-py` es perfecta.

La estrategia es:

1. **Cargar Documentos**: Iterar sobre todos los archivos `.md` en la carpeta `docs-md-py`.
2. **Fragmentar (Chunking)**: Dividir cada archivo por sus encabezados Markdown (ej. `##`).
3. **Incrustar (Embeddings)**: Convertir los textos a vectores usando modelos como `text-embedding-3-small` de OpenAI.
4. **Base Vectorial**: Guardar los vectores en una base de datos local como [ChromaDB](https://docs.trychroma.com/) o FAISS.

### Ejemplo de Snippet en Python (LangChain)

```python
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter

# 1. Cargar todos los archivos markdown
loader = DirectoryLoader('./docs-md-py', glob="**/*.md", show_progress=True)
docs = loader.load()

# 2. Dividir respetando la estructura Markdown
headers_to_split_on = [("#", "Header 1"), ("##", "Header 2")]
markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

chunks = []
for doc in docs:
    splits = markdown_splitter.split_text(doc.page_content)
    # Aquí puedes añadir los metadatos del archivo original a cada chunk
    chunks.extend(splits)

print(f"Total de fragmentos (chunks) listos para la Vector DB: {len(chunks)}")

# 3. (Siguiente paso): Enviar 'chunks' a ChromaDB, Pinecone, o FAISS.
```

---

## ⚠️ Consejos Clave para Prompters

- **Usa el índice**: Si estás usando un modelo con ventana de contexto enorme (ej. Gemini 1.5 Pro), puedes pasarle primero el `GUIDE_INDEX.md` (que es muy ligero) y pedirle: _"Revisa este índice y dime qué archivos .md exactos necesitas que te proporcione para responder mi pregunta"_.
- **Mantén la metadata**: El scraper dejó los links fuente (`> Source: ...`) al inicio de cada archivo. Úsalo en tus prompts: _"Cuando me respondas, por favor cita la URL de Epic Games de donde sacaste la información usando la metadata del archivo"_.
