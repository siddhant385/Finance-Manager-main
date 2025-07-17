# your_project/nodes/behavior_node.py

from typing import List
from .BaseNode import BaseNode
from ..prompts.Base import BasePrompt
from ..prompts.behaviourPrompt import BehaviourPrompt

class BehaviorNode(BaseNode):
    """
    This class requires NO changes. It automatically works with DeepResearchState.
    """
    def _get_prompt_handler(self) -> BasePrompt:
        return BehaviourPrompt()

    def _get_input_keys(self) -> List[str]:
        return self.prompt_handler.input_variables()

    def _get_output_key(self) -> str:
        return "behavior"
    