# src/ai.py

from .Ai.graph import graph  # your compiled LangGraph
from typing import Dict
import asyncio

class AI:
    def __init__(self):
        pass

    def advisor(self, user_answers: Dict) -> Dict:
        """
        Run the financial advisor agent with user input.
        This is a synchronous wrapper for the async graph.
        """
        input_state = {
            "user_data": user_answers  # Updated to match new state format
        }
        
        # Run the async graph in a synchronous context
        result = asyncio.run(graph.ainvoke(input_state))

        return {
            "collector_data": result.get("collector_data"),
            "transaction": result.get("transaction"),
            "behavior": result.get("behavior"),
            "goal": result.get("goal"),
            "advice": result.get("advice"),
            "report": result.get("report"),
            "report_eval": result.get("report_eval")
        }
