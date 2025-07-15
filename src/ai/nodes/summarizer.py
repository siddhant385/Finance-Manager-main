from ..prompts import PromptFamily
from pydantic import ValidationError
import json

class SummarizerNode:
    def __init__(self, llm):
        self.llm = llm

    def __call__(self, state: dict) -> dict:
        prompt = PromptFamily.generate_summary_prompt(state)
        
        response = self.llm.invoke(prompt).content

        print("📤 Generated Final Report:\n", response[:500])  # preview only

        return {
            "final_report_markdown": response
        }
