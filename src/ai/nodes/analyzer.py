from ..prompts import PromptFamily
from ..schemas.analyzer import AnalyzerResponse
from ..utils.json_utils import extract_json

import json
from pydantic import ValidationError

class AnalyzerNode:
    def __init__(self, llm):
        self.llm = llm

    def __call__(self, state: dict) -> dict:
        user = state["collector_data"]["additional_user_data"]
        finance = state["collector_data"]["financial_data"]
        data_to_be_given = {"user_query":user,"finance":finance}
        prompt = PromptFamily.generate_analyzer_prompt(data_to_be_given)

        response = self.llm.invoke(prompt).content  # Use ChatGroq / OpenAI / DeepSeek etc.


        try:
            json_data = json.loads(extract_json(response))
            validated = AnalyzerResponse(**json_data)
            return {
                "analysis_result": validated.dict()
            }

        except (json.JSONDecodeError, ValidationError) as e:
            # Log the error and return a fallback result
            print("❌ LLM response invalid:", e)

            return {
                "analysis_result": {
                    "error": "LLM failed to return valid JSON.",
                    "raw_response": response
                },**state
            }






    

