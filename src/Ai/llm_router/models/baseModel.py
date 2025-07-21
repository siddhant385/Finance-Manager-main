from abc import ABC, abstractmethod
import os
from dotenv import load_dotenv
import logging

# Simple logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BaseModel(ABC):
    """
    Simple base class for all LLM model implementations.
    """
    
    def __init__(self):
        """Initialize the model"""
        load_dotenv()
        
        # Standard parameters for all models
        self.model = "default-model"
        self.temperature = 0.0
        self.max_tokens = None
        self.timeout = None
        self.max_retries = 2
        
        # Initialize the LLM - will be set by subclasses
        self.llm = None
        
        try:
            # Initialize the LLM using the abstract method in subclasses
            self.llm = self._initialize_llm()
            logger.info(f"{self.__class__.__name__} initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize {self.__class__.__name__}: {e}")
            self.llm = None
            
    @abstractmethod
    def _initialize_llm(self):
        """Initialize and return the LLM instance"""
        pass
