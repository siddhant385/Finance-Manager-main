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
                desc TEXT,
                type TEXT CHECK(type IN ('income', 'expense')) NOT NULL           
            );
        """)
        self.conn.commit()

    def insert_data(self, tag, amount, date, desc, type):
        self.cursor.execute(
            "SELECT 1 FROM finance_manager WHERE tag=? AND amount=? AND date=? AND desc=? AND type=?",
            (tag, amount, date, desc, type)
        )
        exists = self.cursor.fetchone()

        if not exists:
            self.cursor.execute(
                "INSERT INTO finance_manager (tag, amount, date, desc, type) VALUES (?, ?, ?, ?, ?)",
                (tag, amount, date, desc ,type)
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
        

    def update_by_id(self,id:int,tag:str,amount:float,date:str,desc:str,type:str):
        self.cursor.execute(
            "UPDATE finance_manager SET tag = ?, amount = ?, date= ?, desc= ?, type= ? WHERE id = ?;",
            (tag,amount,date,desc,type,id)
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
    
    def fetch_total_income(self):
        self.cursor.execute("SELECT SUM(amount) FROM finance_manager WHERE type = 'income';")
        return self.cursor.fetchone()[0] or 0

    def fetch_total_expense(self):
        self.cursor.execute("SELECT SUM(amount) FROM finance_manager WHERE type = 'expense';")
        return self.cursor.fetchone()[0] or 0

    def fetch_all_tags(self):
        self.cursor.execute(
            "SELECT DISTINCT tag FROM finance_manager;"
        )
        return self.cursor.fetchall()
    
    def close(self):
        self.conn.close()
    
    def get_monthly_trend(self):
        self.dbmanager.cursor.execute("""
            SELECT strftime('%Y-%m', date) AS month,
                SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END) AS total_income,
                SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) AS total_expense
            FROM finance_manager
            GROUP BY month
            ORDER BY month;
        """)
        return self.dbmanager.cursor.fetchall()


    def fetch_average_income_per_month(self):
        self.cursor.execute("""
            SELECT AVG(monthly_income) FROM (
                SELECT strftime('%Y-%m', date) AS month,
                    SUM(amount) AS monthly_income
                FROM finance_manager
                WHERE type = 'income'
                GROUP BY month
            );
        """)
        return self.cursor.fetchone()[0] or 0

    def fetch_average_expense_per_month(self):
        self.cursor.execute("""
            SELECT AVG(monthly_expense) FROM (
                SELECT strftime('%Y-%m', date) AS month,
                    SUM(amount) AS monthly_expense
                FROM finance_manager
                WHERE type = 'expense'
                GROUP BY month
            );
        """)
        return self.cursor.fetchone()[0] or 0


    def fetch_top_tags_by_expense(self, limit=5):
        self.cursor.execute("""
            SELECT tag, SUM(amount) as total
            FROM finance_manager
            WHERE type = 'expense'
            GROUP BY tag
            ORDER BY total DESC
            LIMIT ?;
        """, (limit,))
        return self.cursor.fetchall()
    
    def fetch_last_n_months_trend(self, n=3):
        self.cursor.execute(f"""
            SELECT strftime('%Y-%m', date) AS month,
                SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END) AS income,
                SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) AS expense
            FROM finance_manager
            GROUP BY month
            ORDER BY month DESC
            LIMIT {n};
        """)
        return self.cursor.fetchall()
    
    def fetch_large_expenses(self, threshold=10000):
        self.cursor.execute("""
            SELECT * FROM finance_manager
            WHERE type = 'expense' AND amount >= ?;
        """, (threshold,))
        return self.cursor.fetchall()






    
