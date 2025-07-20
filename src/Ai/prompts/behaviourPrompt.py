# financial_prompt.py
from .Base import BasePrompt
from ..schemas.behavior import Behavior

class BehaviourPrompt(BasePrompt):
    def schema(self):
        return Behavior

    def input_variables(self):
        return ["user_data"]

    def system_prompt(self) -> str:
        return """Profile user financially from: {user_data}

Determine:
• Financial archetype: Cautious Saver/Impulsive Spender/Strategic Planner/etc
• Risk tolerance: Low/Medium/High based on stated preferences
• Primary focus: Short-term needs vs long-term goals
• Key traits: Decision patterns, spending triggers, discipline level
• Justify each classification

{format_instructions}"""

