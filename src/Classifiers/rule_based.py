from .base import BaseClassifier
from ..config import CATEGORY_KEYWORDS

class RuleBasedTagClassifier(BaseClassifier):
    def __init__(self, keyword_map=None):
        self.keyword_map = keyword_map or CATEGORY_KEYWORDS

    def classify(self, description: str) -> str:
        desc = description.lower()
        for tag, keywords in self.keyword_map.items():
            for word in keywords:
                if word in desc:
                    return tag
        return "unknown"
