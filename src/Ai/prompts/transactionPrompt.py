# financial_prompt.py
from .Base import BasePrompt
from ..schemas.transaction import Transaction

class transactionPrompt(BasePrompt):
    def schema(self):
        return Transaction

    def input_variables(self):
        return ["collector_data"]

    def system_prompt(self) -> str:
        return """Analyze financial data: {collector_data}

Extract key patterns:
• Spending spikes: monthly/category anomalies
• Essential vs discretionary spending ratio  
• Income-expense stability and trends
• Savings consistency: positive/negative/declining
• Large transactions: one-time expenses >10% monthly income

{format_instructions}"""
