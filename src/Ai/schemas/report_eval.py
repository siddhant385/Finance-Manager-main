from pydantic import BaseModel, Field
from typing import Dict, Any

# Example output format:
# {
#   "is_report_consistent": true,
#   "tone_check": "Pass (Reassuring and positive)",
#   "actionability_score": 8.5,
#   "clarity_score": 9.0,
#   "completeness_score": 8.0,
#   "professionalism_score": 9.5,
#   "language_score": 9.0,
#   "ai_generated_score": 8.5,
#   "feedback": "The report is well-structured and the advice directly links to the analysis. Could provide more specific numbers in the goal steps.",
#   "is_completed": true
# }

class ReportEval(BaseModel):
    is_report_consistent: bool = Field(..., description="Indicates if the report is consistent with the user's profile and goals")
    tone_check: str = Field(..., description="Evaluation of the report's tone")
    actionability_score: float = Field(..., description="Score indicating how actionable the advice in the report is")
    clarity_score: float = Field(..., description="Score indicating the clarity of the report")
    completeness_score: float = Field(..., description="Score indicating how complete the report is")
    professionalism_score: float = Field(..., description="Score indicating the professionalism of the report")
    language_score: float = Field(..., description="Score indicating the quality of language used in the report")
    ai_generated_score: float = Field(..., description="Score indicating how well the AI-generated content meets expectations")
    overall_score: float = Field(..., description="Overall score of the report based on various criteria")
    feedback: str = Field(..., description="Feedback on the report's quality and areas for improvement")
    is_completed: bool = Field(..., description="Indicates if the report evaluation process is completed")