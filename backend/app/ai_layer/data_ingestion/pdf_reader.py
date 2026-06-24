import logging
import warnings
from ai_layer.embeddings.text_splitter import chunk_documents

warnings.filterwarnings(
    "ignore",
    category=DeprecationWarning
)

from langchain_community.document_loaders import (
    PDFPlumberLoader,
    DirectoryLoader
)


# Logger Configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


def load_documents(data_path="../../data"):
    """
    Load all PDF files from data directory.
    """

    logger.info("Starting document loading...")
    logger.info(f"Reading PDFs from: {data_path}")

    loader = DirectoryLoader(
        data_path,
        glob="**/*.pdf",
        loader_cls=PDFPlumberLoader
    )

    documents = loader.load()

    logger.info(f"Successfully loaded {len(documents)} documents")

    return documents


if __name__ == "__main__":

    logger.info("PDF Processing Started")

    documents = load_documents()

    chunks = chunk_documents(documents)

    logger.info(
        f"Documents Loaded: {len(documents)}"
    )

    logger.info(
        f"Chunks Created: {len(chunks)}"
    )

    logger.info("PDF Processing Completed Successfully")