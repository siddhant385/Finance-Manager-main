from abc import ABC, abstractmethod


class Base(ABC):
    def __init__(self,file_path):
        self.file_path = file_path
        
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def sanitize_data(self):
        pass

    @abstractmethod
    def standardize_data(self):
        pass

    @abstractmethod
    def entries(self):
        pass


    
