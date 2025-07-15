# src/ai.py

from .Ai.graph import graph  # your compiled LangGraph
from typing import Dict

class AI:
    def __init__(self):
        pass

    def advisor(self, user_answers: Dict) -> Dict:
        """
        Run the financial advisor agent with user input.
        """
        input_state = {
            "user_answers": user_answers
        }
        result = graph.invoke(input_state)

        return {
            "analysis_result": result.get("analysis_result"),
            "goal_planner_result": result.get("goal_planner_result"),
            "final_advice": result.get("final_advice"),
            "report": result.get("final_report_markdown")
        }
