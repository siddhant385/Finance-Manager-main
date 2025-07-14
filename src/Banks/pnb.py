from .base import Base
from datetime import datetime
import csv
import os

class PNB(Base):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.__data = []
    

    def read_by_csv(self):
        self.__data.clear()
        with open(self.file_path,'r') as f:
            lines = f.readlines()
            start_index =-1
            end_index = -1
            for n,row in enumerate(lines):
                if "Transaction Date" in row:
                    start_index = n
                elif "Unless" in row:
                    end_index = n
            if start_index == -1:
                raise ValueError("Transaction history Not Found")
            transaction_history = lines[start_index:end_index]
            reader = csv.DictReader(transaction_history,skipinitialspace=True)
            for transaction in reader:
                self.__data.append(transaction)
    

    def read(self):
        extension_name = os.path.splitext(self.file_path)[1][1:].lower()  # gives 'csv' or 'pdf'
        if extension_name == "csv":
            self.read_by_csv()
        elif extension_name == "pdf":
            raise NotImplementedError("The following Format is not Implemented Till Now")
        else:
            raise ValueError("Unknown Extension Used")


    
    def sanitize_data(self):
        self.__entries = []
        for data in self.__data:
            if data.get('Withdrawal'):
                self.__entries.append([data.get('Transaction Date'),data.get('Withdrawal'),data.get('Narration')])

    
    def standardize_data(self):
        for data in self.__entries:
            data[0] = datetime.strptime(data[0], "%d/%m/%Y").strftime("%Y-%m-%d")
            data[1] = float(data[1].strip().replace(",",""))

    @property
    def entries(self):
        """returns in order date money desc"""
        self.read()
        self.sanitize_data()
        self.standardize_data()
        return self.__entries
    

