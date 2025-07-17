from pydantic import BaseModel, Field
from typing import List, Dict, Any, Literal

# // Key: "user_profile"
# {
#   "financial_archetype": "Cautious Saver",
#   "risk_tolerance": "Low",
#   "short_term_goal_focus": "Building an emergency fund.",
#   "long_term_goal_focus": "Saving for a down payment.",
#   "behavioral_trait": "User is generally disciplined but can be influenced by large, infrequent purchase opportunities. Shows risk-averse behavior."
# }

class Behavior(BaseModel):
    financial_archetype: str = Field(..., description="User's financial archetype")
    risk_tolerance: str = Field(..., description="User's risk tolerance level")
    short_term_goal_focus: str  = Field(..., description="User's focus on short-term financial goals")
    long_term_goal_focus: str   = Field(..., description="User's focus on long-term financial goals")
    behavioral_trait: str = Field(..., description="User's behavioral traits and tendencies")