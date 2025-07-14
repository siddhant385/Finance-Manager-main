from .databaseManager import DatabaseManager
from .importer import Importer
from src.config import DB_PATH


class FinanceManager:
    def __init__(self):
        self.dbmanager = DatabaseManager(DB_PATH)
        self.dbmanager.create_table()
        
    def extract_bank_statement_to_db(self,file,bankname):
        self.importer = Importer(file,bankname)
        for date,amount,desc,tag in self.importer.entries:
            self.add_data(tag,amount,date,desc)

    def add_data(self,tag,amount,date,desc):
        self.dbmanager.insert_data(tag,amount,date,desc)
    
    def update_data(self,id,tag,amount,date,desc):
        self.dbmanager.update_by_id(id,tag,amount,date,desc)

    def delete_data(self,id):
        self.dbmanager.delete_by_id(id)

    def get_all_data(self):
        data = self.dbmanager.fetch_all_data()
        return data
    def get_all_tags(self):
        data = self.dbmanager.fetch_all_tags()
        return data
    
    def filter_by_month(self,month):
        data = self.dbmanager.fetch_by_month(month)
        return data
    
    def filter_by_date(self,date):
        data = self.dbmanager.fetch_by_date(date)
        return data
    
    def get_total_expense(self):
        data = self.dbmanager.fetch_total_amount()
        return data
    
    def summary_by_tag(self,tag):
        data = self.dbmanager.fetch_by_tag(tag)
        print(data)
        return data
    
    
    


    