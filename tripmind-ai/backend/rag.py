import sys
from unittest.mock import MagicMock

# Workaround for Langchain bug on Windows (imports Unix-only 'pwd' module)
if sys.platform == "win32":
    sys.modules["pwd"] = MagicMock()

import os
from dotenv import load_dotenv

# Load .env from project root
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# Ensure GOOGLE_API_KEY is set for LangChain
if not os.getenv("GOOGLE_API_KEY"):
    gemini_key = os.getenv("GEMINI_API_KEY", "")
    if gemini_key:
        os.environ["GOOGLE_API_KEY"] = gemini_key

CHROMA_DB_DIR = os.path.join(os.path.dirname(__file__), "data", "chroma_db")
DOCS_DIR = os.path.join(os.path.dirname(__file__), "data", "travel_docs")

os.makedirs(CHROMA_DB_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)

# Try importing ChromaDB components
CHROMA_AVAILABLE = False
try:
    import glob
    from langchain_community.document_loaders import PyPDFLoader
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
    from langchain_core.prompts import PromptTemplate
    from langchain_core.runnables import RunnablePassthrough
    from langchain_core.output_parsers import StrOutputParser

    try:
        from langchain_chroma import Chroma
        CHROMA_AVAILABLE = True
    except ImportError:
        try:
            from langchain_community.vectorstores import Chroma
            CHROMA_AVAILABLE = True
        except ImportError:
            CHROMA_AVAILABLE = False

except ImportError as e:
    print(f"[WARNING] RAG dependency missing: {e}")


class TravelKnowledgeBase:
    def __init__(self):
        self.vector_store = None
        self.retriever = None
        self.rag_chain = None

    def initialize(self):
        """Initialize the RAG pipeline."""
        if not CHROMA_AVAILABLE:
            print("[INFO] ChromaDB not available. RAG will use fallback mode.")
            return

        try:
            embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
            self.vector_store = Chroma(
                collection_name="travel_knowledge",
                embedding_function=embeddings,
                persist_directory=CHROMA_DB_DIR
            )

            # Ingest documents if collection is empty
            if self.vector_store._collection.count() == 0:
                self._ingest_documents()
            else:
                count = self.vector_store._collection.count()
                print(f"[OK] Loaded {count} chunks from knowledge base.")

            self.retriever = self.vector_store.as_retriever(search_kwargs={"k": 3})

            llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
            prompt = PromptTemplate.from_template(
                "You are a travel assistant. Use the Context to answer the Question.\n"
                "If you don't know, say so. Be concise.\n\n"
                "Context: {context}\nQuestion: {question}\nAnswer:"
            )

            def format_docs(docs):
                return "\n\n".join(doc.page_content for doc in docs)

            self.rag_chain = (
                {"context": self.retriever | format_docs, "question": RunnablePassthrough()}
                | prompt
                | llm
                | StrOutputParser()
            )
            print("[OK] RAG pipeline initialized.")
        except Exception as e:
            print(f"[WARNING] RAG initialization failed: {e}")

    def _ingest_documents(self):
        """Load and ingest PDFs."""
        pdf_files = glob.glob(os.path.join(DOCS_DIR, "*.pdf"))
        if not pdf_files:
            print("[INFO] No PDFs found. Skipping ingestion.")
            return

        all_docs = []
        for pdf_path in pdf_files:
            print(f"Loading {pdf_path}...")
            loader = PyPDFLoader(pdf_path)
            all_docs.extend(loader.load())

        if all_docs:
            splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
            splits = splitter.split_documents(all_docs)
            print(f"Adding {len(splits)} chunks to vector store...")
            self.vector_store.add_documents(documents=splits)
            print("[OK] Ingestion complete.")


# Global instance
_knowledge_base = TravelKnowledgeBase()


def init_rag():
    """Called on server startup."""
    try:
        _knowledge_base.initialize()
    except Exception as e:
        print(f"[WARNING] RAG init error (non-fatal): {e}")


def query_travel_knowledge(query: str) -> str:
    """Query the travel knowledge base."""
    if not _knowledge_base.rag_chain:
        return "Knowledge base not available."
    try:
        return _knowledge_base.rag_chain.invoke(query)
    except Exception as e:
        return f"Knowledge base query failed: {str(e)}"
