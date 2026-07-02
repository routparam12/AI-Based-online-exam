import json


class QuestionValidator:

    @staticmethod
    def validate(response):

        try:
            questions = json.loads(response)

            if not isinstance(questions, list):
                raise ValueError("Response must be a list.")

            return questions

        except Exception as e:
            raise ValueError(f"Invalid LLM Response: {e}")