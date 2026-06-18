from langchain_chroma import Chroma

class ChromaStore:

    def create_vectorstore(
        self,
        docs,
        embeddings
    ):

        return Chroma.from_documents(
            docs,
            embeddings,
            persist_directory="data/chroma"
        )
