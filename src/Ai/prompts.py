import json

class PromptFamily:
    """General purpose class for prompt formatting.

    This may be overwritten with a derived class that is model specific. The
    methods are broken down into two groups:

    1. Prompt Generators: These follow a standard format and are correlated with
        the ReportType enum. They should be accessed via
        get_prompt_by_report_type

    2. Prompt Methods: These are situation-specific methods that do not have a
        standard signature and are accessed directly in the agent code.

    All derived classes must retain the same set of method names, but may
    override individual methods.
    """

    @staticmethod
    def generate_analyzer_prompt(query:str):
        """
        Generate prompt for LLM-based MCP tool selection.
        
        Args:
            query: The data and the information given
        Returns:
            str: The analyzer prompt
        """
        return f"""You are a research assistant helping to select the most relevant tools for a research query.
FINANCIAL DATA: "{query}"

TASK: Analyze the above information and generate a structured response based on the following criteria:
ANALYZATION CRITERIA:

- User's main goal and urgency
- Time horizon to achieve goal
- Risk tolerance (based on income-expense gap and savings)
- Overspending patterns (e.g., top expense tags too high?)
- Budgeting needs (does user lack discipline?)
- Realism of goal (is current state enough to achieve goal?)
- Emotional bias (is the goal impulsive or well-thought?)
- **CRITICAL: Always check if monthly savings is negative - if so, budgeting and expense control must be prioritized**

RESPONSE FORMAT (Output *only* this JSON block format — no explanation, no extra text):
```json
{{
  "goal_type": "purchase",
  "goal_detail": "Buy a bike",
  "time_horizon": "short_term",
  "risk_estimate": "high",
  "needs_budgeting_help": true,
  "realistic_goal": false,
  "current_savings_deficit": true,
  "reasoning_summary": "User is spending too much in 'transfer' category. Goal is not feasible in 2 months without saving more.",
  "recommended_next": ["goal_based_planner", "expense_optimizer"]
}}
```"""

    def generate_goal_plan_prompt(analyzer_result: dict):
        return f"""
You are a financial planning assistant helping the user achieve their financial goals.

USER GOAL PROFILE:
{json.dumps(analyzer_result, indent=2)}

TASK:
Design a structured and feasible goal plan based on the following criteria:

🔹 GOAL IDENTIFICATION
- Classify the goal as short-term (1-3 yrs), mid-term (3-7 yrs), or long-term (10+ yrs)
- Understand the goal purpose from user's input

🔹 GOAL QUANTIFICATION
- Estimate target amount based on realistic market prices (laptop = ₹60K-₹100K, car = ₹8L-₹15L etc.)
- Use reasonable assumptions if not explicitly given
- **IMPORTANT: For laptops, use realistic price ranges, not inflated amounts**

🔹 INFLATION ADJUSTMENT
- Apply inflation only for goals beyond 2 years
- For goals within 1-2 years, use current market price
- Future Value (FV) = Present Value × (1 + r)^n (only if n > 2)

🔹 MONTHLY SAVINGS NEEDED
- Calculate monthly investment needed using future value formula
- **CRITICAL: If user has negative savings, clearly state this makes goal unfeasible**
- Don't suggest investment amounts higher than what user can realistically save

🔹 RECOMMENDATION
- Be honest about feasibility - if user has deficit, goal is not feasible without expense control
- Prioritize expense management over investment suggestions for deficit situations

🎯 RESPONSE FORMAT ((Output *only* this JSON block format — no explanation, no extra text)):
```json
{{
  "goal_category": "short_term",
  "goal_name": "Buy a laptop for AI work",
  "target_amount": 80000,
  "time_years": 1,
  "inflation_applied": false,
  "future_value": 80000,
  "monthly_saving_required": 6667,
  "current_monthly_savings": -45000,
  "is_feasible": false,
  "feasibility_gap": 51667,
  "recommendations": [
    "URGENT: Address monthly deficit of ₹45,000 before considering investments",
    "Reduce 'transfer' expenses by ₹50,000+ monthly",
    "Only after achieving positive savings, start goal-based saving"
  ]
}}
```"""

    def generate_advice_prompt(analysis_result: dict, goal_plan: dict, user_query: dict) -> str:
        return f"""
You are a certified financial advisor assistant. Your job is to give practical, personalized investment and planning advice based on the user's profile.

📌 INPUT:
USER GOAL PROFILE:
{json.dumps(analysis_result, indent=2)}

GOAL PLAN:
{json.dumps(goal_plan, indent=2)}

USER QUERY:
{json.dumps(user_query, indent=2)}

TASK:
Give advice in the following 6 categories by looking at the user's financial situation, goals, and preferences.

**CRITICAL RULES:**
1. If user has negative savings, prioritize expense control over investment advice
2. Don't suggest investments when user can't save money
3. Address specific behavioral issues mentioned by user (e.g., food habits)
4. Be realistic about what's achievable given current financial state

CATEGORIES:
1. **Expense Management** (PRIORITY if negative savings)
2. Investment Allocation (only if positive savings possible)
3. Insurance Needs (basic coverage only if affordable)
4. Tax Planning (only if applicable to income level)
5. Emergency Fund (build only after expense control)
6. Action Plan (immediate steps prioritized by urgency)

🎯 RESPONSE FORMAT (JSON only):
```json
{{
  "expense_management": "URGENT: Reduce transfer expenses by ₹50,000/month. Address food habit concerns with budgeting apps and cash-only spending.",
  "investment_advice": "Not recommended until positive savings achieved. Focus on expense control first.",
  "insurance_advice": "Basic term life insurance only after achieving positive cash flow.",
  "tax_planning": "Utilize 80C deductions if eligible, but prioritize cash flow management.",
  "emergency_fund": "Build ₹30,000 emergency fund only after achieving ₹10,000+ monthly savings.",
  "action_plan": [
    "IMMEDIATE: Analyze and reduce transfer expenses by ₹50,000/month",
    "Week 1: Implement food spending controls using cash-only method",
    "Month 1: Achieve positive monthly savings of ₹10,000+",
    "Month 2: Start building emergency fund",
    "Month 3: Consider goal-based savings only if cash flow is stable"
  ]
}}
```"""
    
    def generate_summary_prompt(state: dict) -> str:
        return f"""
You are a professional financial advisor preparing a formal Financial Planning Report for a client based on the data below.

📦 DATA:
COLLECTOR DATA:
{json.dumps(state["collector_data"], indent=2)}

ANALYSIS RESULT:
{json.dumps(state["analysis_result"], indent=2)}

GOAL PLAN:
{json.dumps(state["goal_planner_result"], indent=2)}

ADVICE:
{json.dumps(state["final_advice"], indent=2)}

📝 TASK:
Write a comprehensive **financial summary report** based on the structure below. Keep the tone friendly and personalized, but professional.

**CRITICAL REQUIREMENTS:**
1. **BE HONEST** - If user has negative savings, clearly state goals are not feasible without expense control
2. **PRIORITIZE CORRECTLY** - Address expense management before investment suggestions
3. **USE ACCURATE DATA** - Don't contradict the provided financial data
4. **ADDRESS USER CONCERNS** - Specifically mention and provide solutions for stated behavioral issues
5. **REALISTIC RECOMMENDATIONS** - Don't suggest investments when user can't save money

📘 STRUCTURE:
1. 📝 Cover Page (use dummy client name if not specified)
2. 📌 Executive Summary (honest assessment of current situation)
3. 💰 Current Financial Snapshot (accurate data representation)
4. 📊 Cash Flow Analysis (highlight deficit if present)
5. 🎯 Goal Planning Summary (realistic feasibility assessment)
6. 📈 Investment Recommendations (only if applicable)
7. 🛡️ Insurance & Risk Cover (basic coverage suggestions)
8. 💼 Tax Planning Suggestions (relevant to income level)
9. 📅 Action Plan & Timeline (prioritized by urgency)

🧠 IMPORTANT:
- Use bullet points / tables where possible
- Explain *why* a recommendation is made briefly
- Don't add extra tips — stick to the data
- **NEVER suggest investments when user has negative savings**
- **ALWAYS address specific behavioral concerns mentioned by user**
- Include disclaimer about AI-generated content

📤 OUTPUT FORMAT:
Return the final report as a clean string in markdown format (for easy PDF export later).

**QUALITY CHECKS:**
- Does the report honestly assess the current financial situation?
- Are recommendations realistic given the user's cash flow?
- Does it address the user's specific behavioral concerns?
- Are calculations accurate and consistent?
- Is the tone helpful but realistic about challenges?
"""