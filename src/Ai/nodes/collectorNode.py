from ...financeManager import FinanceManager




class CollectorNode:
    def __init__(self):
        # self.tools = tools_registry  # tool name → callable
        self.fm = FinanceManager()

        
    def __call__(self, state):
        # Handle both dictionary and Pydantic model state formats
        if hasattr(state, 'get'):
            # Dictionary format (legacy)
            answers = state.get("user_answers")
        else:
            # Pydantic model format (new)
            answers = getattr(state, 'user_data', None)
            
        income = self.fm.get_total_income()
        expense = self.fm.get_total_expense()
        savings = self.fm.get_savings()
        trend = self.fm.get_last_n_months_trend()
        top_tags = self.fm.get_top_expense_tags()
        big_txns = self.fm.get_large_expenses()

        structured_data = {
            "additional_user_data": answers,
            "financial_data": {
                "income": income,
                "expense": expense,
                "savings": savings,
                "monthly_trend": trend,
                "top_expense_tags": top_tags,
                "large_transactions": big_txns,
            }
        }

        return {
            "collector_data": structured_data
        }

        
