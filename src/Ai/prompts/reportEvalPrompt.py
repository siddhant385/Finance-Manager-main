from .Base import BasePrompt
from ..schemas.report_eval import ReportEval

class ReportEvalPrompt(BasePrompt):
    def schema(self):
        return ReportEval

    def input_variables(self):
        return ["report"]

    def system_prompt(self) -> str:
        return """Evaluate report quality: {report}

Score (0-10) each:
• Consistency with user data
• Tone appropriateness  
• Actionability of recommendations
• Clarity and readability
• Completeness and structure
• Professional presentation
• Language quality
• AI-generated output standards

Set is_completed=true if overall_score ≥7.

Feedback requirements:
- If score <7: Provide specific, actionable improvement suggestions
- Mention exactly what needs to be fixed (tone, missing data, unclear recommendations, etc.)
- Be constructive and specific, not generic
- If score ≥7: Brief positive confirmation

{format_instructions}"""
