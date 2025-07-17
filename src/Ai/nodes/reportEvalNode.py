# your_project/nodes/report_eval_node.py

from typing import List
from .BaseNode import BaseNode
from ..prompts.Base import BasePrompt
from ..prompts.reportEvalPrompt import ReportEvalPrompt

class ReportEvalNode(BaseNode):
    """
    This class requires NO changes. It automatically works with DeepResearchState.
    """
    def _get_prompt_handler(self) -> BasePrompt:
        return ReportEvalPrompt()

    def _get_input_keys(self) -> List[str]:
        # It reads from the 'report' attribute of the DeepResearchState object.
        return ["report"]

    def _get_output_key(self) -> str:
        return "report_eval"
    