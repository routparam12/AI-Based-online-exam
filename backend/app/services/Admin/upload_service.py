import os
import logging

from fastapi import UploadFile

from app.ai_layer.data_ingestion.pdf_reader import (
    load_documents,
    chunk_documents
)
from app.ai_layer.embeddings.embedding_service import (
    get_embedding_model
)
from app.ai_layer.vectorstore.chroma_store import (
    create_vector_store
)

logger = logging.getLogger(__name__)

UPLOAD_DIR = "app/data"


async def upload_pdf_service(file: UploadFile):

    # Save PDF
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as f:
        f.write(await file.read())

    logger.info(f"Saved PDF: {file.filename}")

    # Load PDF
    documents = load_documents(UPLOAD_DIR)

    # Chunk PDF
    chunks = chunk_documents(documents)

    # Embedding Model
    embedding_model = get_embedding_model()

    # Store in Chroma
    create_vector_store(
        chunks,
        embedding_model
    )

    return {
        "message": "PDF uploaded successfully",
        "file_name": file.filename,
        "documents": len(documents),
        "chunks": len(chunks)
    }