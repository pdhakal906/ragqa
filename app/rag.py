import tempfile
import os

from mistralai import Mistral

from app.models.document import Document
from app.models.document_chunks import DocumentChunk
from app.utils import extract_text, chunk_text, get_embedding
from app.config import settings
from app.database import SessionLocal


MISTRAL_API_KEY = settings.MISTRAL_API_KEY
client = Mistral(api_key=MISTRAL_API_KEY)


async def process_pdf(file) -> int:
    """
    Process a PDF file: extract text, chunk it, generate embeddings, and store in DB.
    Returns the document ID.
    """
    # Create a temporary file to save the uploaded PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        contents = await file.read()
        temp_file.write(contents)
        temp_path = temp_file.name

    try:
        # Extract text from PDF
        text_content = extract_text(temp_path)

        # Create document record
        session = SessionLocal()
        try:
            document = Document(filename=file.filename)
            session.add(document)
            session.commit()
            session.refresh(document)
            document_id = document.id

            # Chunk the text
            chunks = chunk_text(text_content, chunk_size=500, overlap=100)

            # Generate embeddings and store chunks
            for chunk_content in chunks:
                embedding = get_embedding(chunk_content)
                chunk_record = DocumentChunk(
                    document_id=document_id, content=chunk_content, embedding=embedding
                )
                session.add(chunk_record)

            session.commit()
            return document_id

        finally:
            session.close()
    finally:
        # Clean up temporary file
        os.unlink(temp_path)


async def ask_question(document_id: int, question: str) -> str:
    """
    Answer a question based on a document's chunks using vector similarity search.
    """
    session = SessionLocal()
    try:
        # Embed the question
        question_embedding = get_embedding(question)

        result = (
            session.query(DocumentChunk.content)
            .filter(DocumentChunk.document_id == document_id)
            .order_by(DocumentChunk.embedding.l2_distance(question_embedding))
            .limit(5)
            .all()
        )

        context_chunks = [row[0] for row in result]

        # Generate answer using GPT
        context = "\n\n".join(context_chunks)
        prompt = f"""Use the following context to answer the question.
If the answer is not in the context, say you don't know.

Context:
{context}

Question:
{question}
"""

        response = client.chat.complete(
            model="mistral-large-latest",
            messages=[{"role": "user", "content": prompt}],
        )

        return response.choices[0].message.content

    finally:
        session.close()
