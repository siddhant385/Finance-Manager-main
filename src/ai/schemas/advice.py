from pydantic import BaseModel
from typing import List



class AdviceResponse(BaseModel):
    expense_management: str
    investment_advice: str
    insurance_advice: str
    tax_planning: str
    emergency_fund: str
    action_plan: List[str]
