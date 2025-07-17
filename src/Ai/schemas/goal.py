import json
from pydantic import BaseModel, ValidationError, Field
from typing import List, Dict, Optional

# // Key: "generated_goals"
# [
#   {
#     "goal_title": "Complete Emergency Fund",
#     "linked_profile_goal": "Building an emergency fund",
#     "realistic_target": "give user a realistic target based on their financial situation",
#     "user_defined_timeframe": "unrealistic",
#     "honest_assessment": "user has negative savings, so this goal is unrealistic at the moment",
#     "goal_category": "short_term",
#     "steps": [
#       "Calculate 3 months of essential expenses.",
#       "Set up an automatic monthly transfer of 15% of your net savings.",
#       "Track progress monthly."
#     ],
#     "priority": "High"
#   }
# ]

class Goal(BaseModel):
    goal_title: str = Field(..., description="Title of the financial goal")
    linked_profile_goal: str = Field(..., description="Goal linked to user's financial profile")
    realistic_target: str = Field(..., description="Realistic target based on user's financial situation")
    user_defined_timeframe: str = Field(..., description="User-defined timeframe for the goal")
    honest_assessment: str = Field(..., description="Honest assessment of the goal's feasibility")
    goal_category: str = Field(..., description="Category of the goal (e.g., short_term, long_term)")
    steps: List[str] = Field(..., description="Steps to achieve the goal")
    priority: str = Field(..., description="Priority level of the goal (e.g., High, Medium, Low)")
