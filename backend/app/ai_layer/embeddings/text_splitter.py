# app/ai_layer/embeddings/text_splitter.py

import logging

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


# --------------------------------------------------
# Logger Configuration
# --------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# --------------------------------------------------
# Document Chunking Function
# --------------------------------------------------

def chunk_documents(
    documents,
    chunk_size=500,
    chunk_overlap=50
):


    logger.info("Starting document chunking...")
    logger.info(
        f"Chunk Size: {chunk_size}, "
        f"Chunk Overlap: {chunk_overlap}"
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = splitter.split_documents(documents)

    logger.info(
        f"Generated {len(chunks)} chunks successfully."
    )

    return chunks


# --------------------------------------------------
# Testing
# --------------------------------------------------

if __name__ == "__main__":

    # PDF Path
    pdf_path = "../../data/cat_and_alien_story.pdf"

    logger.info("Loading PDF...")

    # Load PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    logger.info(
        f"PDF Loaded Successfully. "
        f"Pages Found: {len(documents)}"
    )

    # Split PDF into chunks
    chunks = chunk_documents(
        documents=documents,
        chunk_size=500,
        chunk_overlap=50
    )

    print("\n" + "=" * 60)
    print(f"TOTAL CHUNKS CREATED: {len(chunks)}")
    print("=" * 60)

    # Display chunk information
    for index, chunk in enumerate(chunks):

        print(f"\nChunk #{index + 1}")
        print("-" * 60)

        print(
            f"Characters: "
            f"{len(chunk.page_content)}"
        )

        print("\nContent Preview:\n")

        print(chunk.page_content[:300])

        print("\n" + "-" * 60)

    logger.info("Chunking test completed successfully.")