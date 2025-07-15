import streamlit as st
from src.ai import AI
from src.financeManager import FinanceManager
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="💰 Finance Tool", layout="wide")
st.title("💰 AI-Powered Financial Manager")

fm = FinanceManager()
ai = AI()

# Tabs
tab1, tab2, tab3 = st.tabs(["🧠 AI Advisor", "📊 Finance Dashboard", "🧾 Manage Records"])

# =====================
# 🧠 AI ADVISOR SECTION
# =====================
with tab1:
    st.header("AI-Powered Financial Advisor")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("👤 Your Name")
        age = st.text_input("🎂 Your Age")
        goal = st.text_input("🎯 Financial Goal")
        goal_timeline = st.selectbox("📅 Timeline", ["6 months", "1 year", "2-5 years", "More than 5 years"])
        risk_style = st.radio("📉 Risk Reaction", [
            "❌ Panic and withdraw everything — I can't tolerate loss",
            "🕒 Do nothing — I will wait for recovery",
            "📈 Invest more — I see it as an opportunity"
        ])

    with col2:
        habit_concern = st.text_area("⚠️ Spending Concern")
        income_source = st.selectbox("💼 Income Source", ["Salary", "Business", "Freelancing", "Other", "No Income"])
        income_stability = st.selectbox("📊 Income Stability", ["Yes, almost the same", "No, it fluctuates"])
        dependents = st.selectbox("👪 Financial Dependents", ["0", "1", "2", "3 or more"])
        existing_commitments = st.text_area("📄 Loans/Investments")

    if st.button("🚀 Generate AI Report"):
        if goal and goal_timeline and habit_concern:
            with st.spinner("Generating your financial report..."):
                user_data = {
                    "name": name,
                    "age": age,
                    "goal": f"{goal} (Timeline: {goal_timeline})",
                    "risk_question": risk_style,
                    "bad_habit_concern": habit_concern,
                    "income_source": income_source,
                    "income_stability": income_stability,
                    "dependents": dependents,
                    "existing_commitments": existing_commitments
                }
                result = ai.advisor({"user_answers": user_data})
                st.success("✅ Report Ready!")

                # FINAL REPORT
                st.markdown("### 📄 Final Report")
                st.markdown(result.get("report", "❌ No report found."))

                # FINAL ADVICE
                final_advice = result.get("final_advice", {})
                if final_advice:
                    st.markdown("### 🧠 Final Advice")
                    st.markdown(f"**💸 Expense Management:** {final_advice['expense_management']}")
                    st.markdown(f"**📈 Investment Advice:** {final_advice['investment_advice']}")
                    st.markdown(f"**🛡️ Insurance Advice:** {final_advice['insurance_advice']}")
                    st.markdown(f"**💰 Tax Planning:** {final_advice['tax_planning']}")
                    st.markdown(f"**🚨 Emergency Fund:** {final_advice['emergency_fund']}")
                    st.markdown("**🧩 Action Plan:**")
                    for step in final_advice["action_plan"]:
                        st.markdown(f"- {step}")

                # ANALYSIS RESULT
                analysis = result.get("analysis_result", {})
                if analysis:
                    st.markdown("### 📊 Goal Analysis")
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**🎯 Goal Type:** {analysis['goal_type']}")
                        st.markdown(f"**📝 Goal Detail:** {analysis['goal_detail']}")
                        st.markdown(f"**⏳ Time Horizon:** {analysis['time_horizon']}")
                        st.markdown(f"**⚖️ Risk Estimate:** {analysis['risk_estimate']}")
                    with col2:
                        st.markdown(f"**💡 Needs Budgeting Help:** {'✅ Yes' if analysis['needs_budgeting_help'] else '❌ No'}")
                        st.markdown(f"**✅ Realistic Goal:** {'✅ Yes' if analysis['realistic_goal'] else '❌ No'}")
                        st.markdown(f"**🪙 Savings Deficit:** {'✅ Yes' if analysis['current_savings_deficit'] else '❌ No'}")
                    st.markdown(f"**🧠 Summary:** {analysis['reasoning_summary']}")
                    st.markdown("**🧭 Recommendations:**")
                    for r in analysis["recommended_next"]:
                        st.markdown(f"- {r}")

                # GOAL PLANNER RESULT
                goal_plan = result.get("goal_planner_result", {})
                if goal_plan:
                    st.markdown("### 🎯 Goal Planner Output")
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**🏷️ Category:** {goal_plan['goal_category']}")
                        st.markdown(f"**📌 Goal Name:** {goal_plan['goal_name']}")
                        st.markdown(f"**🎯 Target Amount:** ₹{goal_plan['target_amount']:,}")
                        st.markdown(f"**📅 Time Horizon:** {goal_plan['time_years']} years")
                        st.markdown(f"**📈 Inflation Adjusted:** {'✅ Yes' if goal_plan['inflation_applied'] else '❌ No'}")
                        st.markdown(f"**🔮 Future Value:** ₹{goal_plan['future_value']:,}")
                    with col2:
                        st.markdown(f"**💸 Monthly Saving Needed:** ₹{goal_plan['monthly_saving_required']:,}")
                        st.markdown(f"**💼 Current Saving:** ₹{goal_plan['current_monthly_savings']:,}")
                        st.markdown(f"**✅ Feasible:** {'✅ Yes' if goal_plan['is_feasible'] else '❌ No'}")
                        st.markdown(f"**⚠️ Gap:** ₹{goal_plan['feasibility_gap']:,}")
                    st.markdown("**📋 Recommendations:**")
                    for rec in goal_plan["recommendations"]:
                        st.markdown(f"- {rec}")
        else:
            st.warning("❗ Please fill all required fields.")


# =========================
# 📊 DASHBOARD/ANALYTICS TAB
# =========================
with tab2:
    st.header("📊 Financial Summary Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Total Income", f"₹{fm.get_total_income()}")
    col2.metric("💸 Total Expense", f"₹{fm.get_total_expense()}")
    col3.metric("💼 Savings", f"₹{fm.get_savings()}")

    st.subheader("📈 Monthly Trend")
    trend = fm.get_last_n_months_trend()
    if trend:
        df_trend = pd.DataFrame(trend, columns=["Month", "Income", "Expense"])
        st.line_chart(df_trend.set_index("Month"))
    else:
        st.info("No trend data available.")

    st.subheader("🔝 Top Expense Categories")
    tags = fm.get_top_expense_tags()
    if tags:
        tag_df = pd.DataFrame(tags, columns=["Tag", "Amount"])
        st.bar_chart(tag_df.set_index("Tag"))
    else:
        st.warning("No expenses yet.")

    st.subheader("⚠️ Large Expenses (₹10,000+)")
    big_txns = fm.get_large_expenses()
    if big_txns:
        st.dataframe(pd.DataFrame(big_txns, columns=["ID", "Tag", "Amount", "Date", "Desc", "Type"]))
    else:
        st.success("No large transactions found.")

# ============================
# 🧾 RECORD MANAGEMENT SECTION
# ============================
with tab3:
    st.header("🧾 Manage Records")

    # Add New Entry
    with st.expander("➕ Add Transaction"):
        tag = st.text_input("Tag")
        amount = st.number_input("Amount", min_value=0.0, step=100.0)
        date = st.date_input("Date", value=datetime.today())
        desc = st.text_input("Description")
        ttype = st.radio("Type", ["income", "expense"])
        if st.button("✅ Add Entry"):
            fm.add_data(tag, amount, date.strftime("%Y-%m-%d"), desc, ttype)
            st.success("Entry Added!")

    # View All
    with st.expander("📋 View All Transactions"):
        all_data = fm.get_all_data()
        if all_data:
            df_all = pd.DataFrame(all_data, columns=["ID", "Tag", "Amount", "Date", "Desc", "Type"])
            st.dataframe(df_all)
        else:
            st.info("No entries available.")

    # Filter by Month
    with st.expander("📅 Filter by Month"):
        selected_month = st.text_input("Month (Format: YYYY-MM)")
        if selected_month:
            results = fm.filter_by_month(selected_month)
            if results:
                st.dataframe(pd.DataFrame(results, columns=["ID", "Tag", "Amount", "Date", "Desc", "Type"]))
            else:
                st.warning("No entries for this month.")

    # Delete
    with st.expander("❌ Delete Entry"):
        del_id = st.number_input("ID to Delete", min_value=1)
        if st.button("🗑️ Delete"):
            fm.delete_data(del_id)
            st.success(f"Entry ID {del_id} deleted.")

    # Update
    with st.expander("✏️ Update Entry"):
        update_id = st.number_input("ID to Update", min_value=1)
        new_tag = st.text_input("New Tag")
        new_amount = st.number_input("New Amount", min_value=0.0)
        new_date = st.date_input("New Date", value=datetime.today(), key="update_date")
        new_desc = st.text_input("New Description")
        new_type = st.radio("New Type", ["income", "expense"], key="update_type")
        if st.button("✏️ Update Entry"):
            fm.update_data(update_id, new_tag, new_amount, new_date.strftime("%Y-%m-%d"), new_desc, new_type)
            st.success("Updated successfully.")

    # Export
    with st.expander("💾 Export to CSV"):
        export_path = st.text_input("Export Path", value="exported.csv")
        if st.button("📤 Export"):
            fm.export_data(export_path)
            st.success(f"Exported to {export_path}")

    # Import
    with st.expander("📥 Import Statement"):
        uploaded_file = st.file_uploader("Upload CSV")
        bank_name = st.text_input("Bank Name (e.g., pnb)")
        if st.button("📥 Import"):
            if uploaded_file and bank_name:
                import_path = f"/tmp/{uploaded_file.name}"
                with open(import_path, "wb") as f:
                    f.write(uploaded_file.read())
                fm.extract_bank_statement_to_db(import_path, bank_name)
                st.success("Imported successfully!")
            else:
                st.warning("Upload file and enter bank name.")

