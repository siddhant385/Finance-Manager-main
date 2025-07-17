from pydantic import BaseModel, Field
from typing import List, Dict, Optional

# // Key: "final_report"
# {
#   "report_title": "Your Personalized Financial Health Analysis",
#   "report_description": "A comprehensive report summarizing your financial health, goals, and actionable advice.",
#   "report_tone": "based on the user's financial archetype, the report is presented in a reassuring and informative tone.", 
#   "professionalism": "The report is structured to provide clear insights and actionable steps.",
#   "language_tone": "The language used is simple and easy to understand, avoiding jargon and technicalities as well as human-like.",
#   "final_report": "A markdown formatted report summarizing the user's financial health, goals, and actionable advice."
# }

class FinalReport(BaseModel):
  report_title: str = Field(..., description="Title of the financial report")
  report_description: str = Field(..., description="Description of the financial report")
  report_tone: str = Field(..., description="Tone of the report based on the user's financial archetype")
  professionalism: str = Field(..., description="Professionalism level of the report")
  language_tone: str = Field(..., description="Language used in the report")
  final_report: str = Field(..., description="Markdown formatted report summarizing the user's financial health, goals, and actionable advice")