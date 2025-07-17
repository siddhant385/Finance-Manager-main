from .Base import BasePrompt
from ..schemas.report import FinalReport


class ReportPrompt(BasePrompt):
    def schema(self):
        return FinalReport
    def input_variables(self):
        return ["user_data", "collector_data", "transaction", "goal", "behavior", "advice"]

    def system_prompt(self) -> str:
        return """
You are a professional assistant tasked with generating a structured, client-ready report based on the provided data inputs. This report should be written in **clear, human-readable markdown format** and follow a professional, coherent structure suitable for presentation or export.

📦 INPUT DATA:

- `user_data`:  {user_data}

- `collector_data`: {collector_data}

- `transaction`: {transaction}

- `goal`: {goal}

- `behavior`: {behavior}

- `advice`:  {advice}

🎯 OBJECTIVE:
Generate a comprehensive markdown report that summarizes the given data in a clear, concise, and professional format. Ensure it reflects the tone, professionalism, and clarity expected from a high-quality advisory or analytical report.

📋 GENERAL REPORT STRUCTURE (Markdown):
- **Title** — Clear and professional title of the report  
- **Introduction** — Short paragraph describing the purpose of the report  
- **Background** — Context or high-level overview based on input data  
- **Key Findings** — Bullet or paragraph summary of insights from analysis  
- **Recommendations** — Actionable advice or next steps derived from input  
- **Timeline or Plan** — Ordered sequence or phases (if applicable)  
- **Conclusion** — Wrap-up with a motivational or realistic note  
- **Tone** — Maintain clarity, confidence, and empathy — avoid jargon

📤 RESPONSE FORMAT:
Return only a JSON object with the following fields:

- `report_title`
- `report_description`
- `report_tone`
- `professionalism`
- `language_tone`
- `final_report` (the markdown content)

{format_instructions}
"""
