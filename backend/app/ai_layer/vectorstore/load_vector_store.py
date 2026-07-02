from langchain_chroma import Chroma

from app.ai_layer.embeddings.embedding_service import create_embeddings


def load_vector_store():

    return Chroma(
        persist_directory="./chroma_db",
        embedding_function=create_embeddings()
    )