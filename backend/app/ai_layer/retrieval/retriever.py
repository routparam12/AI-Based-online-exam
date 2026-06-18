class Retriever:

    def get_context(
        self,
        vectorstore,
        query
    ):

        docs = vectorstore.similarity_search(
            query,
            k=5
        )

        return "\n".join(
            [doc.page_content for doc in docs]
        )
