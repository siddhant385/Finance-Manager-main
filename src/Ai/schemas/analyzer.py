from pydantic import BaseModel
from typing import List



class AnalyzerResponse(BaseModel):
    goal_type: str
    goal_detail: str
    time_horizon: str
    risk_estimate: str
    needs_budgeting_help: bool
    realistic_goal: bool
    current_savings_deficit:bool
    reasoning_summary: str
    recommended_next: List[str]
