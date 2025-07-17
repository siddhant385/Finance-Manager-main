# financial_prompt.py
from .Base import BasePrompt
from ..schemas.transaction import Transaction

class transactionPrompt(BasePrompt):
    def schema(self):
        return Transaction

    def input_variables(self):
        return ["collector_data"]

    def system_prompt(self) -> str:
        return """
You are a financial research assistant helping to analyze user transactions for deeper insight into their financial behavior.

FINANCIAL DATA: "{collector_data}"

TASK:
Analyze the above information and generate a structured response based on the following criteria.

ANALYSIS CRITERIA:

- Spending patterns over time: Are there spikes in spending in any specific months or categories?
- Category concentration: Are expenses concentrated in essentials (e.g. Rent, Food) or non-essentials?
- Monthly income vs expenses trend: Is spending stable, increasing, or erratic?
- Savings behavior: Are savings consistent, declining, or negative?
- Anomalies: Identify one-time large expenses or significant deviations from the usual patterns.

RESPONSE FORMAT:
Output only a JSON object in the format below. Do not include any extra explanation or text.

{format_instructions}
"""
