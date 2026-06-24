import logging

from langchain_chroma import Chroma
from matplotlib import path

from ai_layer.embeddings.text_splitter import chunk_documents

logger = logging.getLogger(__name__)


def create_vector_store(
    chunks,
    embedding_model
):
    """
    Create Chroma vector database.
    """

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="./chroma_db"
    )

    logger.info(
        f"Stored {len(chunks)} chunks in ChromaDB"
    )

    return vector_store

if __name__ == "__main__":
    
    create_vector_store(chunk_documents())
