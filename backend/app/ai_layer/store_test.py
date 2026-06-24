from app.ai_layer.data_ingestion.pdf_reader import (
    load_documents,
    chunk_documents
)

from app.ai_layer.embeddings.embedding_service import (
    embedding_model
)

from app.ai_layer.vectorstore.chroma_store import (
    create_vector_store
)


documents = load_documents()

chunks = chunk_documents(documents)

embedding_model = embedding_model()

vector_store = create_vector_store(
    chunks,
    embedding_model
)

print("Vector Store Ready")