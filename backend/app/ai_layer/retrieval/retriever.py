class Retriever:

    def get_context(
        self,
        vectorstore,
        query,
        k=5
    ):

        docs = vectorstore.similarity_search(
            query=query,
            k=k
        )

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        return context


