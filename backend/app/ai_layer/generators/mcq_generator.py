from ai_layer.prompts.question_generation import MCQ_PROMPT

class MCQGenerator:

    async def generate(
        self,
        llm,
        context,
        difficulty,
        count
    ):

        prompt = MCQ_PROMPT.format(
            context=context,
            difficulty=difficulty,
            count=count
        )

        response = await llm.ainvoke(prompt)

        return response.content