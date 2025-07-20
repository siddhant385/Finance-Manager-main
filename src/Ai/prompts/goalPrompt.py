# financial_prompt.py
from .Base import BasePrompt
from ..schemas.goal import Goal

class GoalPrompt(BasePrompt):
    def schema(self):
        return Goal

    def input_variables(self):
        return ["user_data", "collector_data", "transaction", "behavior"]

    def system_prompt(self) -> str:
        return """Create financial goal plan from:
User: {user_data} | Data: {collector_data} | Analysis: {transaction}, {behavior}

For each goal:
• Realistic target based on current savings rate
• Honest feasibility: if savings ≤0, focus on expense reduction first
• Timeline: short (1-3yr), mid (3-7yr), long (10+yr)
• Priority: High/Medium/Low based on urgency + importance
• Actionable steps matching user's archetype

{format_instructions}"""
