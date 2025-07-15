from ..utils.json_utils import extract_json
from ..prompts import PromptFamily
from ..schemas.goalPlanner import GoalPlannerResponse

from pydantic import ValidationError
import json

class GoalPlannerNode:
    def __init__(self, llm):
        self.llm = llm

    def __call__(self, state: dict) -> dict:
        analyzer_result = state["analysis_result"]
        user = state["collector_data"]["additional_user_data"]
        finance = state["collector_data"]["financial_data"]
        data_to_be_given = {"user_query":user,"finance":finance,"analysis":analyzer_result}
        prompt = PromptFamily.generate_goal_plan_prompt(data_to_be_given)
        response = self.llm.invoke(prompt).content

        try:
            json_data = json.loads(extract_json(response))
            validated = GoalPlannerResponse(**json_data)
            return {
                "goal_planner_result": validated.dict()
            }

        except (json.JSONDecodeError, ValidationError) as e:
            # Log the error and return a fallback result
            print("❌ LLM response invalid:", e)

            return {
                "goal_planner_result": {
                    "error": "LLM failed to return valid JSON.",
                    "raw_response": response
                } ,**state
            }

