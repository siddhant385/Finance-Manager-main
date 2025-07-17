# your_project/nodes/goal_node.py

from typing import List
from .BaseNode import BaseNode
from ..prompts.Base import BasePrompt
from ..prompts.goalPrompt import GoalPrompt

class GoalNode(BaseNode):
    """
    This class requires NO changes. It automatically works with DeepResearchState.
    """
    def _get_prompt_handler(self) -> BasePrompt:
        return GoalPrompt()

    def _get_input_keys(self) -> List[str]:
        return ["user_data", "collector_data", "transaction", "behavior"]

    def _get_output_key(self) -> str:
        return "goal"
    