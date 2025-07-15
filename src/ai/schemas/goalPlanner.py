from pydantic import BaseModel
from typing import List




class GoalPlannerResponse(BaseModel):
    goal_category: str
    goal_name: str
    target_amount: int
    time_years: float
    inflation_applied: bool
    future_value: int
    monthly_saving_required: int
    current_monthly_savings: int
    is_feasible: bool
    feasibility_gap: int
    recommendations: List[str]
