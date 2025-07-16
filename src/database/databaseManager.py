
from peewee import fn, Case
from .models import Finance, db


# To make this a runnable, self-contained file, the database and model
# definitions are included here. In a real application, these would
# likely be in a separate 'models.py' file.

class DatabaseManager:
    def insert_data(self, tag, amount, date, desc, transaction_type):
        with db.connection_context():
            exists = Finance.select().where(
                (Finance.tag == tag) &
                (Finance.amount == amount) &
                (Finance.date == date) &
                (Finance.desc == desc) &
                (Finance.type == transaction_type)
            ).exists()

            if not exists:
                Finance.create(
                    tag=tag,
                    amount=amount,
                    date=date,
                    desc=desc,
                    type=transaction_type
                )
                return True
            return False

    def delete_by_id(self, id):
        with db.connection_context():
            query = Finance.delete().where(Finance.id == id)
            query.execute()

    def update_by_id(self, id, tag, amount, date, desc, transaction_type):
        with db.connection_context():
            query = Finance.update({
                Finance.tag: tag,
                Finance.amount: amount,
                Finance.date: date,
                Finance.desc: desc,
                Finance.type: transaction_type
            }).where(Finance.id == id)
            query.execute()

    def fetch_all_data(self):
        with db.connection_context():
            return list(Finance.select().dicts())
    
    def fetch_data_by_id(self, id):
        with db.connection_context():
            return Finance.select().where(Finance.id == id).get()

    def fetch_by_date(self, date):
        with db.connection_context():
            return list(Finance.select().where(Finance.date == date).dicts())

    def fetch_by_month(self, month):
        with db.connection_context():
            return list(Finance.select().where(
                fn.strftime('%Y-%m', Finance.date) == month
            ).dicts())

    def fetch_by_tag(self, tag):
        with db.connection_context():
            return list(Finance.select().where(Finance.tag == tag).dicts())

    def fetch_total_income(self):
        with db.connection_context():
            return Finance.select(fn.SUM(Finance.amount)).where(Finance.type == 'income').scalar() or 0

    def fetch_total_expense(self):
        with db.connection_context():
            return Finance.select(fn.SUM(Finance.amount)).where(Finance.type == 'expense').scalar() or 0

    def fetch_all_tags(self):
        with db.connection_context():
            return [entry['tag'] for entry in Finance.select(Finance.tag).distinct().dicts()]

    def get_monthly_trend(self):
        with db.connection_context():
            return list(Finance.select(
                fn.strftime('%Y-%m', Finance.date).alias('month'),
                fn.SUM(Case(None, [(Finance.type == 'income', Finance.amount)], 0)).alias('total_income'),
                fn.SUM(Case(None, [(Finance.type == 'expense', Finance.amount)], 0)).alias('total_expense')
            ).group_by(fn.strftime('%Y-%m', Finance.date)).order_by(fn.strftime('%Y-%m', Finance.date)).dicts())

    def fetch_average_income_per_month(self):
        with db.connection_context():
            subquery = (
                Finance
                .select(
                    fn.strftime('%Y-%m', Finance.date).alias('month'),
                    fn.SUM(Finance.amount).alias('monthly_income')
                )
                .where(Finance.type == 'income')
                .group_by(fn.strftime('%Y-%m', Finance.date))
            ).alias('monthly_summary')

            query = (
                Finance.select(fn.AVG(subquery.c.monthly_income))
                .from_(subquery)
            )
            average = query.scalar()
            return average or 0

    def fetch_average_expense_per_month(self):
        with db.connection_context():
            subquery = (
                Finance
                .select(
                    fn.strftime('%Y-%m', Finance.date).alias('month'),
                    fn.SUM(Finance.amount).alias('monthly_expense')
                )
                .where(Finance.type == 'expense')
                .group_by(fn.strftime('%Y-%m', Finance.date))
            ).alias('monthly_summary')

            query = (
                Finance.select(fn.AVG(subquery.c.monthly_expense))
                .from_(subquery)
            )
            average = query.scalar()
            return average or 0

    def fetch_top_tags_by_expense(self, limit=5):
        with db.connection_context():
            return list(Finance.select(
                Finance.tag,
                fn.SUM(Finance.amount).alias('total')
            ).where(Finance.type == 'expense')
            .group_by(Finance.tag)
            .order_by(fn.SUM(Finance.amount).desc())
            .limit(limit).dicts())

    def fetch_last_n_months_trend(self, n=3):
        with db.connection_context():
            month_expr = fn.strftime('%Y-%m', Finance.date)
            return list(Finance.select(
                month_expr.alias('month'),
                fn.SUM(Case(None, [(Finance.type == 'income', Finance.amount)], 0)).alias('income'),
                fn.SUM(Case(None, [(Finance.type == 'expense', Finance.amount)], 0)).alias('expense')
            )
            .group_by(month_expr)
            .order_by(month_expr.desc())
            .limit(n)
            .dicts())

    def fetch_large_expenses(self, threshold=10000):
        with db.connection_context():
            return list(Finance.select().where(
                (Finance.type == 'expense') &
                (Finance.amount >= threshold)
            ).dicts())

if __name__ == "__main__":
    db.connect()
    db.create_tables([Finance], safe=True)
    print("Database and tables created successfully.")
    
    manager = DatabaseManager()

    # Example usage with sample data
    manager.insert_data("Salary", 5000, "2023-10-01", "Monthly pay", "income")
    manager.insert_data("Groceries", 150, "2023-10-05", "Weekly shopping", "expense")
    manager.insert_data("Rent", 1200, "2023-10-01", "Monthly rent", "expense")
    manager.insert_data("Salary", 5000, "2023-11-01", "Monthly pay", "income")
    manager.insert_data("Groceries", 175, "2023-11-06", "Weekly shopping", "expense")
    manager.insert_data("Rent", 1200, "2023-11-01", "Monthly rent", "expense")

    print("\n--- All Data ---")
    all_data = manager.fetch_all_data()
    for row in all_data:
        print(row)
    
    print("\n--- Total Income ---")
    print(manager.fetch_total_income())

    print("\n--- Average Expense Per Month ---")
    print(manager.fetch_average_expense_per_month())

    print("\n--- Deleting entry with ID 2 ---")
    manager.delete_by_id(2)

    print("\n--- All Data After Deletion ---")
    all_data = manager.fetch_all_data()
    for row in all_data:
        print(row)
        
    db.close()