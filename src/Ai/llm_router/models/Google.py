import os
from langchain_google_genai import ChatGoogleGenerativeAI
from .baseModel import BaseModel


class Google(BaseModel):
    """Google Gemini model implementation that extends BaseModel"""
    
    def _initialize_llm(self):
        """Initialize and return the Google Generative AI model"""
        api_key = os.getenv("GOOGLE_API_KEY")
        
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
        
        # Set model name for Google
        self.model = "gemini-2.5-flash"
            
        return ChatGoogleGenerativeAI(
            model=self.model,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            timeout=self.timeout,
            max_retries=self.max_retries,
        )
    