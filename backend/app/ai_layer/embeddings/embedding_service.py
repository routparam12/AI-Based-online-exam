from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

# print(os.getenv("GEMINI_API_KEY"))

embedding_model = GoogleGenerativeAIEmbeddings(
            model="gemini-embedding-2",

        )
vector = embedding_model.embed_documents(
        texts = [
        "Python is a programming language.",
        "FastAPI is a web framework.",
        "LangChain is used for LLM applications."
]
    )



# print(len(vector))

if __name__ == "__main__":

    print(vector)
