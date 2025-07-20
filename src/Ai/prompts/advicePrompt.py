from .Base import BasePrompt
from ..schemas.advice import Advice

class AdvicePrompt(BasePrompt):
    def schema(self):
        return Advice

    def input_variables(self):
        return ["user_data", "collector_data", "transaction", "behavior"]

    def system_prompt(self) -> str:
        return """Generate financial advice from:
Profile: {user_data} | Data: {collector_data} | Analysis: {transaction}, {behavior}

Rules:
• No investments if savings ≤0 (focus on expenses)
• Match tone to user archetype
• Address behavioral blockers directly
• Provide specific, actionable steps

Include: advice title, behavioral solution, implementation steps.

{format_instructions}"""
