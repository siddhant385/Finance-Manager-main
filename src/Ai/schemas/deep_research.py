from pydantic import BaseModel
from typing import Optional, Dict



class DeepResearchState(BaseModel):
    user_data: Optional[Dict] = None
    collector_data: Optional[Dict] = None
    transaction: Optional[Dict] = None
    behavior: Optional[Dict] = None
    emotions: Optional[Dict] = None
    goal: Optional[Dict] = None
    advice: Optional[Dict] = None
    report: Optional[Dict] = None
    report_eval: Optional[Dict] = None
    error : Optional[str] = None
    