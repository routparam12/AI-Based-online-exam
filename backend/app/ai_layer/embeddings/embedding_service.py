# app/ai_layer/embeddings/embedding_service.py
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

from ai_layer.embeddings.text_splitter import chunk_documents
from ai_layer.data_ingestion.pdf_reader import load_documents

load_dotenv()



embedding_model = GoogleGenerativeAIEmbeddings(
            model="gemini-embedding-2",
        )

def create_embeddings(chunks):
    texts = [chunk.page_content for chunk in chunks]
    return embedding_model.embed_documents(texts=texts)



def get_embedding_model():
    return GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

if __name__ == "__main__":
    print("--- Pipeline Started ---")

    documents = load_documents()
    chunks = chunk_documents(documents)
    vectors = create_embeddings(chunks)
    print(vectors)


