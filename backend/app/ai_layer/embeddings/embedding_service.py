# app/ai_layer/embeddings/embedding_service.py
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from ai_layer.embeddings.text_splitter import chunk_documents

load_dotenv()

# print(os.getenv("GEMINI_API_KEY"))

embedding_model = GoogleGenerativeAIEmbeddings(
            model="gemini-embedding-2",

        )

def create_embeddings(chunks):
    """
    Generate embeddings from chunked documents.
    """

    texts = [
        chunk.page_content
        for chunk in chunks
    ]

    vectors = embedding_model.embed_documents(
        texts=texts
    )

    return vectors



# print(len(vector))

if __name__ == "__main__":
    documents = create_embeddings(
        chunks=[

        ]
    )


