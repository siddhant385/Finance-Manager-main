import sqlite3

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS finance_manager (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tag TEXT,
                amount REAL,
                date TEXT,
                desc TEXT
                            
            );
        """)
        self.conn.commit()

    def insert_data(self, tag, amount, date, desc):
        self.cursor.execute(
            "SELECT 1 FROM finance_manager WHERE tag=? AND amount=? AND date=? AND desc=?",
            (tag, amount, date, desc)
        )
        exists = self.cursor.fetchone()

        if not exists:
            self.cursor.execute(
                "INSERT INTO finance_manager (tag, amount, date, desc) VALUES (?, ?, ?, ?)",
                (tag, amount, date, desc)
            )
            self.conn.commit()
            return True  # Successfully inserted
        else:
            return False
    
    def delete_by_id(self,id):
        self.cursor.execute(
            "DELETE FROM finance_manager WHERE id = ?;",
            (id))
        self.conn.commit()
        

    def update_by_id(self,id:int,tag:str,amount:float,date:str):
        self.cursor.execute(
            "UPDATE finance_manager SET tag = ?, amount = ?, date= ? WHERE id = ?;",
            (tag,amount,date,id)
        )
        self.conn.commit()

    def fetch_all_data(self):
        self.cursor.execute("SELECT * from finance_manager;")
        return self.cursor.fetchall()
    
    def fetch_by_date(self,date):
        self.cursor.execute(
            "SELECT * FROM finance_manager WHERE date = ?;",
            (date,))
        return self.cursor.fetchall()
    
    def fetch_by_month(self,month):
        self.cursor.execute(
            "SELECT * FROM finance_manager WHERE strftime('%Y-%m', date) = ?;",
            (month,))
        return self.cursor.fetchall()
    
    def fetch_by_tag(self,tag):
        self.cursor.execute(
            "SELECT * FROM finance_manager WHERE tag = ?;",
            (tag,)
        )
        return self.cursor.fetchall()
    
    def fetch_total_amount(self):
        self.cursor.execute(
            "SELECT SUM(amount) FROM finance_manager;"
        )
        return self.cursor.fetchone()

    def fetch_all_tags(self):
        self.cursor.execute(
            "SELECT DISTINCT tag FROM finance_manager;"
        )
        return self.cursor.fetchall()
    
    def close(self):
        self.conn.close()

