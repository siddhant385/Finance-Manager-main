from pydantic import BaseModel, Field
from typing import List



# // Key: "transaction_analysis"
# {
#   "spending_habits_summary": "The user has consistent income but fluctuating expenses, with a notable spike in the month of September. Spending is heavily concentrated on essential items like 'Rent' and 'Food'.",
#   "savings_pattern": "While there are net savings each month, the savings rate decreased in September, indicating a potential overspending event or a large one-time purchase.",
#   "key_observation": "The user's primary expenses are non-discretionary, but there are occasional large purchases that impact their savings goals."
# }



class Transaction(BaseModel):
    spending_habits_summary: str = Field(..., description="Summary of the user's spending habits.")
    savings_pattern: str = Field(..., description="Description of the user's savings pattern.")
    key_observation: str = Field(..., description="Key observation from the transaction analysis.")

