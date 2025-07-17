# your_project/nodes/report_node.py

from typing import List
from .BaseNode import BaseNode
from ..prompts.Base import BasePrompt
from ..prompts.reportPrompt import ReportPrompt

class ReportNode(BaseNode):
    """
    This class now implements `_get_input_keys` to provide all the
    necessary data to its prompt.
    """
    def _get_prompt_handler(self) -> BasePrompt:
        return ReportPrompt()

    # CHANGED: Implemented the new abstract method.
    def _get_input_keys(self) -> List[str]:
        """
        Returns the list of keys required by the ReportPrompt.
        """
        # This list must match the `input_variables` in your ReportPrompt.
        return [
            "user_data",
            "collector_data",
            "transaction",
            "goal",
            "behavior",
            "advice"
        ]

    def _get_output_key(self) -> str:
        return "report"