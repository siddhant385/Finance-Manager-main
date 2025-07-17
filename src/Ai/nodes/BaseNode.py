# your_project/nodes/base_node.py

from abc import ABC, abstractmethod
from typing import List
from langchain_core.language_models import BaseLanguageModel
from langchain_core.exceptions import OutputParserException
from langchain_core.runnables import Runnable
from langchain.output_parsers import OutputFixingParser
from ..prompts.Base import BasePrompt

# Import your specific Pydantic state model
from ..schemas.deep_research import DeepResearchState

class BaseNode(ABC):
    """
    An abstract base class for nodes, designed to work with a Pydantic state model.
    This version is updated to handle multiple input keys.
    """
    def __init__(self, llm: BaseLanguageModel):
        self.prompt_handler = self._get_prompt_handler()
        prompt = self.prompt_handler.get_prompt()
        base_parser = self.prompt_handler.get_parser()
        self_correcting_parser = OutputFixingParser.from_llm(llm=llm, parser=base_parser)
        self.chain: Runnable = prompt | llm | self_correcting_parser

    # --- Abstract methods ---

    @abstractmethod
    def _get_prompt_handler(self) -> BasePrompt:
        pass

    # CHANGED: This method is now plural and returns a list of strings.
    @abstractmethod
    def _get_input_keys(self) -> List[str]:
        """Specifies which keys to read from the state."""
        pass

    @abstractmethod
    def _get_output_key(self) -> str:
        """Specifies which key to write the output to in the state."""
        pass

    # --- The Updated Shared Execution Logic ---

    async def __call__(self, state: DeepResearchState) -> dict:
        """
        The shared execution logic for all nodes.
        It now reads multiple inputs from the Pydantic state object and
        returns updates for it.
        """
        node_name = self.__class__.__name__
        print(f"---RUNNING {node_name}---")
        
        # CHANGED: Get the list of required input keys.
        input_keys = self._get_input_keys()
        output_key = self._get_output_key()

        # CHANGED: Build the input dictionary for the chain by gathering each
        # required key from the state object. A dictionary comprehension
        # makes this clean and efficient.
        input_data = {key: getattr(state, key) for key in input_keys}

        try:
            # The chain is invoked with the dictionary containing all required inputs.
            result = await self.chain.ainvoke(input_data)
            
            print(f"✅ {node_name} finished successfully.")

            # Special handling for ReportNode to display the generated report
            if node_name == "ReportNode" and hasattr(result, 'final_report'):
                print(f"\n📄 GENERATED REPORT:")
                print("="*60)
                print(result.final_report)
                print("="*60)

            # The return structure remains the same: a dictionary to update the state.
            return {output_key: result.dict()}

        except OutputParserException as e:
            print(f"❌ ERROR in {node_name}: The chain failed to parse the LLM's output.")
            return {
                output_key: { "error": "LLM failed to produce a valid format." },
                "error": f"Error in {node_name}: {str(e)}"
            }