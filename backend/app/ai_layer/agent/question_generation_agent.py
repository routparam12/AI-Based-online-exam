from ai_layer.llm.base import get_llm
from ai_layer.retrieval.retriever import Retriever
from ai_layer.generators.mcq_generator import MCQGenerator
from ai_layer.validators.question_validator import QuestionValidator


class QuestionGenerationAgent:

    def __init__(self):

        self.llm = get_llm()
        self.retriever = Retriever()
        self.generator = MCQGenerator()

    async def generate_questions(
        self,
        vectorstore,
        query,
        difficulty,
        count
    ):

        context = self.retriever.get_context(
            vectorstore=vectorstore,
            query=query
        )

        questions = await self.generator.generate(
            llm=self.llm,
            context=context,
            difficulty=difficulty,
            count=count
        )

        validated_questions = QuestionValidator.validate(
            questions
        )
        return questions