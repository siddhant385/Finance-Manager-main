import streamlit as st

import pandas as pd

import plotly.express as px

from datetime import datetime

import tempfile



# Assuming your project structure is sound, these imports should work.

# Make sure this script is run from the root of your project.

from src.financeManager import FinanceManager


from src.ai import AI



class FinanceApp:

    def __init__(self):

        st.set_page_config(page_title="💰 FinanceAI", layout="wide", initial_sidebar_state="expanded")

        self.fm = FinanceManager()

        self.ai = AI()



        if "ai_report" not in st.session_state:

            st.session_state.ai_report = None

        if "active_tab" not in st.session_state:

            st.session_state.active_tab = "Dashboard"



    def run(self):

        st.title("💰 FinanceAI: Your Personal Financial Manager")



        tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "🧾 Manage Records", "🧠 AI Advisor"])



        with tab1:

            self.render_dashboard()

        with tab2:

            self.render_record_manager()

        with tab3:

            self.render_ai_advisor()



    def render_dashboard(self):

        st.header("Financial Overview")

        all_data = self.fm.get_all_data()



        if not all_data:

            st.info("No financial data found. Add some transactions in the 'Manage Records' tab to get started!")

            return



        df = pd.DataFrame(all_data)

        df['amount'] = pd.to_numeric(df['amount'])

        df['date'] = pd.to_datetime(df['date'])



        total_income = self.fm.get_total_income()

        total_expense = self.fm.get_total_expense()

        savings = self.fm.get_savings()



        col1, col2, col3 = st.columns(3)

        col1.metric("💰 Total Income", f"₹{total_income:,.2f}")

        col2.metric("💸 Total Expense", f"₹{total_expense:,.2f}", delta_color="inverse")

        col3.metric("💼 Net Savings", f"₹{savings:,.2f}")



        st.markdown("---")

        

        col1, col2 = st.columns([2, 1])



        with col1:

            st.subheader("📈 Monthly Trends")

            monthly_trend = df.groupby([pd.Grouper(key='date', freq='M'), 'type'])['amount'].sum().unstack(fill_value=0).reset_index()

            monthly_trend['date'] = monthly_trend['date'].dt.strftime('%Y-%b')

            fig_trend = px.line(monthly_trend, x='date', y=['income', 'expense'], title="Income vs. Expense Over Time",

                                labels={'value': 'Amount (₹)', 'date': 'Month'}, markers=True)

            fig_trend.update_layout(legend_title_text='Transaction Type')

            st.plotly_chart(fig_trend, use_container_width=True)



        with col2:

            st.subheader("📁 Expense Categories")

            expense_df = df[df['type'] == 'expense']

            top_tags = expense_df.groupby('tag')['amount'].sum().nlargest(7).reset_index()

            fig_pie = px.pie(top_tags, names='tag', values='amount', title="Top Expense Categories", hole=0.3)

            fig_pie.update_traces(textposition='inside', textinfo='percent+label')

            st.plotly_chart(fig_pie, use_container_width=True)



        st.subheader("🔍 Transaction Breakdown")

        fig_sunburst = px.sunburst(df, path=['type', 'tag'], values='amount', title="Income & Expense Breakdown by Category")

        st.plotly_chart(fig_sunburst, use_container_width=True)

        

        st.subheader("📄 Recent Transactions")

        st.dataframe(df.sort_values(by='date', ascending=False).head(10))





    def render_record_manager(self):

        st.header("Manage Your Financial Records")

        

        action = st.radio("Choose an action:", ["Add Transaction", "Update/Delete Transaction", "Import/Export Data"], horizontal=True, label_visibility="collapsed")

        

        st.markdown("---")

        

        if action == "Add Transaction":

            with st.form("add_transaction_form", clear_on_submit=True):

                st.subheader("➕ Add a New Transaction")

                tag = st.text_input("Tag (e.g., Salary, Groceries)", key="add_tag")

                amount = st.number_input("Amount", min_value=0.01, step=100.0, key="add_amount")

                date = st.date_input("Date", value=datetime.today(), key="add_date")

                desc = st.text_input("Description", key="add_desc")

                ttype = st.radio("Type", ["expense", "income"], key="add_type", horizontal=True)



                submitted = st.form_submit_button("✅ Add Entry")

                if submitted:

                    if not tag or not amount:

                        st.warning("Tag and Amount are required.")

                    else:

                        self.fm.add_data(tag, amount, date.strftime("%Y-%m-%d"), desc, ttype)

                        st.success(f"Added '{tag}' transaction successfully!")

                        st.rerun()



        elif action == "Update/Delete Transaction":

            st.subheader("✏️ Update or ❌ Delete a Transaction")

            all_data = self.fm.get_all_data()

            if not all_data:

                st.info("No data to manage.")

                return



            df = pd.DataFrame(all_data)

            df['display'] = df['date'].astype(str) + " | " + df['tag'] + " | ₹" + df['amount'].astype(str) + " (" + df['type'] + ")"

            

            option = st.selectbox("Select a transaction to manage:", df['display'], index=None, placeholder="Search for a transaction...")



            if option:

                selected_id = df[df['display'] == option]['id'].iloc[0]

                record = self.fm.get_data_by_id(selected_id)

                

                with st.form("update_form"):

                    st.write(f"**Now editing transaction ID: {record.id}**")

                    new_tag = st.text_input("Tag", value=record.tag)

                    new_amount = st.number_input("Amount", value=record.amount)

                    new_date = st.date_input("Date", value=record.date)

                    new_desc = st.text_input("Description", value=record.desc)

                    new_type = st.radio("Type", ["income", "expense"], index=0 if record.type == "income" else 1, horizontal=True)

                    

                    col1, col2 = st.columns([1,5])

                    with col1:

                        update_submitted = st.form_submit_button("✏️ Update")

                    with col2:

                        delete_submitted = st.form_submit_button("❌ Delete", type="primary")



                    if update_submitted:

                        self.fm.update_data(record.id, new_tag, new_amount, new_date.strftime("%Y-%m-%d"), new_desc, new_type)

                        st.success(f"Transaction ID {record.id} updated!")

                        st.rerun()

                    if delete_submitted:

                        self.fm.delete_data(record.id)

                        st.warning(f"Transaction ID {record.id} deleted!")

                        st.rerun()



        elif action == "Import/Export Data":

            st.subheader("💾 Import or Export Your Data")

            col1, col2 = st.columns(2)

            

            with col1:

                st.markdown("**Export to CSV**")

                all_data = self.fm.get_all_data()

                if all_data:

                    df_export = pd.DataFrame(all_data)

                    csv = df_export.to_csv(index=False).encode('utf-8')

                    st.download_button(

                        label="📤 Download All Data as CSV",

                        data=csv,

                        file_name=f"finance_export_{datetime.now().strftime('%Y%m%d')}.csv",

                        mime="text/csv",

                    )

                else:

                    st.info("No data to export.")



            with col2:

                st.markdown("**Import from Bank Statement**")

                uploaded_file = st.file_uploader("Upload CSV Statement", type="csv")

                bank_name = st.text_input("Bank Name (e.g., pnb)", help="Used by the importer to parse correctly.")

                if st.button("📥 Import Now"):

                    if uploaded_file and bank_name:

                        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmpfile:

                            tmpfile.write(uploaded_file.getvalue())

                            import_path = tmpfile.name

                        

                        try:

                            self.fm.extract_bank_statement_to_db(import_path, bank_name)

                            st.success("Bank statement imported successfully!")

                            st.rerun()

                        except Exception as e:

                            st.error(f"Failed to import: {e}")

                    else:

                        st.warning("Please upload a file and provide the bank name.")





    def render_ai_advisor(self):

        st.header("Your AI-Powered Financial Co-Pilot")

        st.caption("Answer the questions below and our AI will generate a personalized financial health report and action plan for you.")

        

        with st.form("ai_advisor_form"):

            st.subheader("Tell Us About Yourself")

            col1, col2 = st.columns(2)

            with col1:

                goal = st.text_input("🎯 What is your primary financial goal?*", help="e.g., Buy a house, Save for retirement, Create an emergency fund")

                age = st.text_input("🎂 Your Age")

                dependents = st.selectbox("👪 Financial Dependents", ["0", "1", "2", "3 or more"])

                income_source = st.selectbox("💼 Main Income Source", ["Salary", "Business", "Freelancing", "Other", "No Income"])

                

            with col2:

                goal_timeline = st.selectbox("📅 What is the timeline for your goal?", ["< 1 year", "1-3 years", "3-5 years", "5+ years"])

                habit_concern = st.text_area("⚠️ What is your biggest spending concern?", help="e.g., Spending too much on dining out, Impulse shopping online")

                income_stability = st.radio("📊 Is your income stable?", ["Yes, it's consistent", "No, it fluctuates"])

            

            existing_commitments = st.text_area("📄 List any existing loans or major investments", help="e.g., Student loan, Car loan, Mutual Fund SIPs")

            

            submitted = st.form_submit_button("🚀 Generate AI Report")

            if submitted:

                if not goal or not habit_concern:

                    st.warning("Please fill in the required fields marked with *.")

                else:

                    with st.spinner("Your AI Co-Pilot is analyzing your profile and drafting your report..."):

                        user_data = {

                            "goal": f"{goal} (Timeline: {goal_timeline})",

                            "age": age,

                            "dependents": dependents,

                            "income_source": income_source,

                            "income_stability": income_stability,

                            "bad_habit_concern": habit_concern,

                            "existing_commitments": existing_commitments

                        }

                        st.session_state.ai_report = self.ai.advisor({"user_answers": user_data})

        

        if st.session_state.ai_report:

            st.markdown("---")

            st.balloons()

            st.success("Your financial report is ready!")

            report = st.session_state.ai_report



            st.subheader("📝 Executive Summary")
            # Updated to handle new response format from the updated graph
            if "report" in report and isinstance(report["report"], dict):
                report_data = report["report"]
                if "final_report" in report_data:
                    st.markdown(report_data["final_report"])
                else:
                    st.markdown("Report generated successfully but content not available for display.")
            else:
                st.markdown(report.get("report", "No summary available."))



            # Handle advice section with new format
            advice_data = report.get("advice")
            if advice_data and isinstance(advice_data, dict):
                st.subheader("💡 Key Recommendations")
                
                # Display advice information
                if "personalized_advice" in advice_data:
                    st.markdown("**📋 Personalized Advice:**")
                    st.markdown(advice_data["personalized_advice"])
                
                if "implementation_steps" in advice_data:
                    st.markdown("**🧩 Implementation Steps:**")
                    steps = advice_data["implementation_steps"]
                    if isinstance(steps, list):
                        for i, step in enumerate(steps, 1):
                            st.markdown(f"{i}. {step}")
                    else:
                        st.markdown(steps)
                
                # Show goal information if available
                goal_data = report.get("goal")
                if goal_data and isinstance(goal_data, dict):
                    with st.expander("🎯 Your Financial Goals"):
                        if "goal_title" in goal_data:
                            st.markdown(f"**Goal:** {goal_data['goal_title']}")
                        if "realistic_target" in goal_data:
                            st.markdown(f"**Target:** {goal_data['realistic_target']}")
                        if "timeline" in goal_data:
                            st.markdown(f"**Timeline:** {goal_data['timeline']}")
            else:
                # Fallback to old format
                final_advice = report.get("final_advice")
                if final_advice:
                    st.subheader("💡 Key Recommendations")
                    cols = st.columns(3)
                    cols[0].metric("🚨 Emergency Fund", final_advice.get('emergency_fund', 'N/A'))
                    cols[1].metric("📈 Investment Advice", final_advice.get('investment_advice', 'N/A'))
                    cols[2].metric("🛡️ Insurance Advice", final_advice.get('insurance_advice', 'N/A'))

                

                with st.expander("Show detailed action plan"):

                    st.markdown(f"**💸 Expense Management:** {final_advice.get('expense_management', '')}")

                    st.markdown(f"**💰 Tax Planning:** {final_advice.get('tax_planning', '')}")

                    if "action_plan" in final_advice:

                        st.markdown("**🧩 Your Action Plan:**")

                        for i, step in enumerate(final_advice["action_plan"], 1):

                            st.markdown(f"{i}. {step}")



if __name__ == "__main__":

    app = FinanceApp()

    app.run()