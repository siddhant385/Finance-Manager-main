from .Banks.pnb import PNB
from .Classifiers.rule_based import RuleBasedTagClassifier

class Importer:
    def __init__(self,filepath,bank_name):
        self.file_path = filepath
        self.bank_name = bank_name
        self.__bank_class = self.__resolver()
        self.classifier =  RuleBasedTagClassifier()
    
    def __resolver(self):
        if self.bank_name.lower() == "pnb":
            return PNB(self.file_path)
        else:
            raise NotImplementedError("Other Banks aren't supported till now.")
    
    @property
    def entries(self):
        """returns in date amount desc tag"""
        raw_entries = self.__bank_class.entries  # [date, amount, desc]
        tagged_entries = []
        for entry in raw_entries:
            tag = self.classifier.classify(entry[2])  # entry[2] = description
            tagged_entries.append([entry[0], entry[1], entry[2], tag])
        return tagged_entries


