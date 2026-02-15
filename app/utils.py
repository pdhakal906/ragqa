from pypdf import PdfReader

from sentence_transformers import SentenceTransformer


embedding_model = SentenceTransformer("BAAI/bge-small-en-v1.5")


def extract_text(file_path: str) -> str:
    """Extract text from a PDF file."""
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100) -> list[str]:
    """Split text into overlapping chunks."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks


def get_embedding(text: str):
    embedding = embedding_model.encode(
        text, normalize_embeddings=True  # important for cosine similarity
    )
    return embedding.tolist()
