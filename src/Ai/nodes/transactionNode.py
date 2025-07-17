# your_project/nodes/transaction_analysis_node.py

from typing import List
from .BaseNode import BaseNode
from ..prompts.Base import BasePrompt
from ..prompts.transactionPrompt import transactionPrompt

class TransactionNode(BaseNode):
    """
    This class requires NO changes. It automatically works with DeepResearchState.
    """
    def _get_prompt_handler(self) -> BasePrompt:
        return transactionPrompt()

    def _get_input_keys(self) -> List[str]:
        # It reads from the 'collector_data' attribute of the DeepResearchState object.
        return ["collector_data"]

    def _get_output_key(self) -> str:
        # It writes its dictionary output to the 'transaction' attribute.
        return "transaction"