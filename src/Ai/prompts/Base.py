# base_prompt.py
from abc import ABC, abstractmethod
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

class BasePrompt(ABC):
    """
    Base class for LangGraph-compatible prompts with schema-bound output parsing.
    """

    def __init__(self):
        self.parser = PydanticOutputParser(pydantic_object=self.schema())
        self.format_instructions = self.parser.get_format_instructions()
        self.prompt = self.build_prompt()

    @abstractmethod
    def schema(self):
        """Return the Pydantic schema class (not instance) used for output parsing."""
        pass

    @abstractmethod
    def system_prompt(self) -> str:
        """Return the base system message with placeholders."""
        pass

    @abstractmethod
    def input_variables(self) -> list:
        """Return a list of variables the prompt expects."""
        pass

    def build_prompt(self) -> ChatPromptTemplate:
        """
        Builds the full ChatPromptTemplate using the format instructions and system prompt.
        """
        template = self.system_prompt()
        return ChatPromptTemplate.from_template(
            template=template,
            partial_variables={"format_instructions": self.format_instructions}
        )

    def get_prompt(self) -> ChatPromptTemplate:
        """Return the final ChatPromptTemplate."""
        return self.prompt

    def get_parser(self) -> PydanticOutputParser:
        """Return the parser to be used in LangGraph."""
        return self.parser
