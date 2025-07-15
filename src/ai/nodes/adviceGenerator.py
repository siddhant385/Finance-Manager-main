from ..prompts import PromptFamily
from ..schemas.advice import AdviceResponse
from ..utils.json_utils import extract_json
from pydantic import ValidationError
import json

class AdviceGeneratorNode:
    def __init__(self, llm):
        self.llm = llm

    def __call__(self, state: dict) -> dict:
        analysis = state["analysis_result"]
        goal_plan = state["goal_planner_result"]
        user_query = state["collector_data"]["additional_user_data"]

        prompt = PromptFamily.generate_advice_prompt(analysis, goal_plan, user_query)
        response = self.llm.invoke(prompt).content

        try:
            json_data = json.loads(extract_json(response))
            validated = AdviceResponse(**json_data)
            return {
                "final_advice": validated.dict(),
                **state
            }

        except (json.JSONDecodeError, ValidationError) as e:
            print("❌ Invalid JSON from LLM:", e)
            return {
                "final_advice": {
                    "error": "LLM returned invalid advice format.",
                    "raw_response": response
                }, **state
            }
