from pydantic import BaseModel, Field
from typing import List



# // Key: "generated_advice"
# [
#   {
#     "for_archetype": "Cautious Saver",
#     "advice_tone": "based on the user's financial archetype, the advice is presented in a cautious and reassuring tone.",
#     "advice_title": "Automate Your Emergency Fund Savings",
#     "advice_details": "Since your goal is to build an emergency fund, set up an automatic transfer of a fixed amount to your savings account on the day you receive your salary. This 'pay yourself first' strategy works well for Cautious Savers.",
#     "behavioral_problems": "Cautious Savers often benefit from automation to avoid the temptation of spending their savings. This aligns with your disciplined nature and helps you stay on track.",
#     "behavioral_solution": "Automating your savings can help you avoid the temptation to spend, especially on large, infrequent purchases that might disrupt your savings plan.",
#     "behavior_solution_steps": [
#       "Practice not to overspend",
#       "Use budgeting apps to track expenses",
#     ],
#     "implementation_steps": [
#       "Set up a recurring transfer of ₹10,000 to your emergency fund account every month.",
#       "Use a high-interest savings account to maximize returns.",
#     ]
#   },
# ]

class Advice(BaseModel):
    for_archetype: str = Field(..., description="Financial archetype for which the advice is tailored")
    advice_tone: str = Field(..., description="Tone of the advice based on the user's financial archetype")
    advice_title: str = Field(..., description="Title of the advice")
    advice_details: str = Field(..., description="Details of the advice")
    behavioral_problems: str = Field(..., description="Behavioral problems identified in the user")
    behavioral_solution: str = Field(..., description="Proposed behavioral solution for the user")
    behavior_solution_steps: List[str] = Field(..., description="Steps to implement the behavioral solution")
    implementation_steps: List[str] = Field(..., description="Steps to implement the advice")