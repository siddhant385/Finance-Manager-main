# financial_prompt.py
from .Base import BasePrompt
from ..schemas.behavior import Behavior

class BehaviourPrompt(BasePrompt):
    def schema(self):
        return Behavior

    def input_variables(self):
        return ["user_data"]

    def system_prompt(self) -> str:
        return """
You are a financial behavior analyst assistant tasked with identifying a user's psychological and strategic approach to money management based on their financial data and actions.

USER PROFILE DATA: "{user_data}"

TASK:
Analyze the above user information and generate a structured psychological and behavioral profile based on the following criteria.

ANALYSIS CRITERIA:

- Financial Archetype: Based on their habits, categorize the user (e.g., Cautious Saver, Impulsive Spender, Strategic Planner, etc.)
- Risk Tolerance: Does the user seem risk-averse, risk-neutral, or risk-seeking?
- Short-Term Focus: What short-term financial goals or patterns are most visible?
- Long-Term Focus: What does the user's behavior suggest about their long-term priorities or concerns?
- Behavioral Traits: Identify personality traits or decision-making tendencies (e.g., disciplined, emotional spender, delay gratification, influenced by peer spending, etc.)

RESPONSE FORMAT:
Output only a JSON object in the format below. Do not include any extra explanation or text.

{format_instructions}
"""

