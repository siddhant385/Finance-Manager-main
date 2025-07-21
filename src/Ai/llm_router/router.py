from typing import Dict, List, Optional, Any
import os
from dotenv import load_dotenv
from langchain_core.language_models import BaseChatModel
import logging

# Import our model classes
from .models.Google import Google
from .models.Groq import Groq

# Simple logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LLMRouter:
    """
    Simple LLM router that loads models based on available API keys
    and provides a unified way to access them for LangChain nodes.
    """
    
    def __init__(self, preferred_provider: str = None):
        """
        Initialize the LLM Router.
        
        Args:
            preferred_provider: Preferred provider to use if available
        """
        # Load environment variables for API keys
        load_dotenv()
        
        # Store preferred provider
        self.preferred_provider = preferred_provider
        
        # Initialize available models
        self.models: Dict[str, Any] = {}
        self._initialize_models()
        
        if self.models:
            logger.info(f"LLM Router initialized with {len(self.models)} models: {', '.join(self.models.keys())}")
        else:
            logger.warning("No LLM models could be initialized. Check your API keys.")
        
    def _initialize_models(self) -> None:
        """Initialize all available models with API keys from environment"""
        # Try to initialize Google model
        try:
            google_model = Google()
            if google_model.llm:  # Check if initialization succeeded
                self.models["google"] = google_model
                logger.info("Google model initialized successfully")
        except Exception as e:
            logger.warning(f"Failed to initialize Google model: {e}")
            
        # Try to initialize Groq model
        try:
            groq_model = Groq()
            if groq_model.llm:  # Check if initialization succeeded
                self.models["groq"] = groq_model
                logger.info("Groq model initialized successfully")
        except Exception as e:
            logger.warning(f"Failed to initialize Groq model: {e}")
            
    def get_langchain_llm(self, preferred_provider: str = None) -> BaseChatModel:
        """
        Get a LangChain-compatible LLM instance.
        
        Args:
            preferred_provider: Optional preferred provider to use if available
            
        Returns:
            LangChain-compatible LLM
        """
        provider_to_use = preferred_provider or self.preferred_provider
        
        # If preferred provider is specified and available, use it
        if provider_to_use and provider_to_use in self.models:
            provider = provider_to_use
        # Otherwise use the first available model
        elif self.models:
            provider = list(self.models.keys())[0]
        else:
            raise ValueError("No LLM models available. Check your API keys.")
            
        logger.info(f"Using {provider} model")
            
        # Return the LangChain-compatible model
        return self.models[provider].llm
        
    def get_available_providers(self) -> List[str]:
        """Get list of available model providers"""
        return list(self.models.keys())
    
    def set_preferred_provider(self, provider: str) -> None:
        """
        Set the preferred provider.
        
        Args:
            provider: Provider name to use by default
        """
        if provider not in self.get_available_providers():
            logger.warning(f"Provider '{provider}' is not available. Setting anyway.")
            
        self.preferred_provider = provider
        logger.info(f"Preferred provider set to: {provider}")
    