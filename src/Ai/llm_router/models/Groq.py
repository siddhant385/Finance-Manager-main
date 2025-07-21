import os
from langchain_groq import ChatGroq
from .baseModel import BaseModel


class Groq(BaseModel):
    """Groq model implementation that extends BaseModel"""
    
    def _initialize_llm(self):
        """Initialize and return the Groq model"""
        api_key = os.getenv("GROQ_API_KEY")
        
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")
        
        # Set model name for Groq
        self.model = "deepseek-r1-distill-llama-70b"
            
        return ChatGroq(
            model=self.model,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            timeout=self.timeout,
            max_retries=self.max_retries,
        )
    
    # Error was here - removed _post_initialize() with self.llm.initialize()