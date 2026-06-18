from langchain_google_genai import GoogleGenerativeAIEmbeddings

class EmbeddingService:

    def get_embedding_model(self):

        return GoogleGenerativeAIEmbeddings(
            model="models/embedding-001"
        )