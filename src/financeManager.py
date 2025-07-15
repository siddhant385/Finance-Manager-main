from .databaseManager import DatabaseManager
from .importer import Importer
from src.config import DB_PATH


class FinanceManager:
    def __init__(self):
        self.dbmanager = DatabaseManager(DB_PATH)
        self.dbmanager.create_table()
        
    def extract_bank_statement_to_db(self,file,bankname):
        self.importer = Importer(file,bankname)
        for amount,date,desc,tag,type in self.importer.entries:
            self.add_data(tag,amount,date,desc,type)

    def add_data(self,tag,amount,date,desc,isIncome):
        if isinstance(isIncome, str) and isIncome in ["income", "expense"]:
            type = isIncome
        else:
            type = "income" if isIncome else "expense"
        self.dbmanager.insert_data(tag,amount,date,desc,type)
    
    def update_data(self,id,tag,amount,date,desc,isIncome):
        """Type could only be income or expense"""
        if isIncome:
            type = "income"
        else:
            type="expense"
        self.dbmanager.update_by_id(id,tag,amount,date,desc,type)

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
        data = self.dbmanager.fetch_total_expense()
        return data
    
    def get_total_income(self):
        data = self.dbmanager.fetch_total_income()
        return data

    def summary_by_tag(self,tag):
        data = self.dbmanager.fetch_by_tag(tag)
        print(data)
        return data
    
    def get_savings(self):
        return self.get_total_income() - self.get_total_expense()
    
    def get_top_expense_tags(self, limit=5):
        return self.dbmanager.fetch_top_tags_by_expense(limit)

    def get_average_monthly_income(self):
        return self.dbmanager.fetch_average_income_per_month()

    def get_average_monthly_expense(self):
        return self.dbmanager.fetch_average_expense_per_month()

    def get_last_n_months_trend(self, n=3):
        return self.dbmanager.fetch_last_n_months_trend(n)

    def get_large_expenses(self, threshold=10000):
        return self.dbmanager.fetch_large_expenses(threshold)


    
    
    


    