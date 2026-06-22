from ai_layer.llm.base import LLMManager
from ai_layer.retrieval.retriever import Retriever
from ai_layer.generators.mcq_generator import MCQGenerator

class QuestionGenerationAgent:

```
def __init__(self):

    self.llm = LLMManager.get_llm()

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

    return questions
```
