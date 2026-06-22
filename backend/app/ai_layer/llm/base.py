from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def get_llm():

    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2,
        max_output_tokens=4096,
    )


if __name__ == "__main__":
    model = get_llm()
    result = model.invoke("hello worked in python")
    print(result.content)
