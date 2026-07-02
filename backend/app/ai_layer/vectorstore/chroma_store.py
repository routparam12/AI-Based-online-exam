# app/ai_layer/vectorstore/chroma_store.py
import logging
from langchain_chroma import Chroma

logger = logging.getLogger(__name__)

def create_vector_store(
    chunks,
    embedding_model
):
    logger.info("ChromaDB data storing...")


    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="./chroma_db"
    )

    logger.info(
        f"Stored {len(chunks)} chunks in ChromaDB"
    )

    return vector_store


def get_vector_store(embedding_model):
    return Chroma(
        persist_directory="./chroma_db",
        embedding_function=embedding_model
    )


