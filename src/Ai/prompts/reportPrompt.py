from .Base import BasePrompt
from ..schemas.report import FinalReport

class ReportPrompt(BasePrompt):
    def schema(self):
        return FinalReport
    
    def input_variables(self):
        return ["user_data", "collector_data", "transaction", "goal", "behavior", "advice", "report_eval"]

    def system_prompt(self) -> str:
        return """Generate professional markdown report from:
{user_data} | {collector_data} | {transaction} | {goal} | {behavior} | {advice}

=== EVALUATION FEEDBACK ===
{report_eval}
=== END FEEDBACK ===

Structure:
• Title & Introduction
• Financial Overview (current state)
• Key Insights (patterns, behavior)
• Recommendations (actionable advice)
• Implementation Plan (timeline, steps)
• Conclusion (motivational, realistic)

Instructions:
- If evaluation feedback appears above between the markers, this is an IMPROVEMENT ITERATION
- Address ALL issues mentioned in the feedback section
- If no feedback (empty between markers), create a comprehensive new report
- Maintain professional, clear, empathetic tone
- Avoid jargon, use actionable language

{format_instructions}"""
