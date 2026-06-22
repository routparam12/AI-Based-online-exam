from langchain_community.document_loaders import PDFPlumberLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = DirectoryLoader(
    "../../data",
    glob="**/*.pdf",
    loader_cls=PDFPlumberLoader
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=300
)

documents = loader.load()

class TextChunker:
    @staticmethod
    def chunk_documents(document):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1500,
            chunk_overlap=300
        )
        return text_splitter.split_documents(document)

if __name__ == "__main__":
    print(documents)
