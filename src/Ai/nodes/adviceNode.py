# your_project/nodes/advice_node.py

from typing import List
from .BaseNode import BaseNode
from ..prompts.Base import BasePrompt
from ..prompts.advicePrompt import AdvicePrompt

class AdviceNode(BaseNode):
    """
    This class requires NO changes. It automatically works with DeepResearchState.
    """
    def _get_prompt_handler(self) -> BasePrompt:
        return AdvicePrompt()

    def _get_input_keys(self) -> List[str]:
        return self.prompt_handler.input_variables()

    def _get_output_key(self) -> str:
        return "advice"
    