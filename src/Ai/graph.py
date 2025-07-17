from .nodes.collectorNode import CollectorNode
from .nodes.behaviorNode import BehaviorNode
from .nodes.transactionNode import TransactionNode
from .nodes.goalNode import GoalNode
from .nodes.adviceNode import AdviceNode
from .nodes.reportNode import ReportNode
from .nodes.reportEvalNode import ReportEvalNode


from langgraph.graph import StateGraph, END, START
from langgraph.types import Send
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from .schemas.deep_research import DeepResearchState


load_dotenv()

llm = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
    # other params...
)

# Using your actual DeepResearchState instead of the old state
# This state model already has all the fields we need


collector_node = CollectorNode()
behavior_node = BehaviorNode(llm)
transaction_node = TransactionNode(llm)
goal_node = GoalNode(llm)
advice_node = AdviceNode(llm)
report_node = ReportNode(llm)
report_eval_node = ReportEvalNode(llm)


builder = StateGraph(DeepResearchState)

# Add all your actual nodes
builder.add_node("collector", collector_node)
builder.add_node("behavior", behavior_node)
builder.add_node("transaction", transaction_node)
builder.add_node("goal", goal_node)
builder.add_node("advice", advice_node)
builder.add_node("report", report_node)
builder.add_node("report_eval", report_eval_node)

# Create intermediate synchronization nodes for coordination
def sync_after_analysis(state):
    """Synchronization point after behavior and transaction"""
    return state  # Just pass through the state

def sync_after_planning(state):
    """Synchronization point after goal and advice"""
    return state  # Just pass through the state

builder.add_node("analysis_sync", sync_after_analysis)
builder.add_node("planning_sync", sync_after_planning)

# Your desired workflow:
# 1. Start with collector
builder.add_edge(START, "collector")

# 2. After collector, run behavior and transaction in parallel
builder.add_edge("collector", "behavior")
builder.add_edge("collector", "transaction")

# 3. Both behavior and transaction flow to sync point
builder.add_edge("behavior", "analysis_sync")
builder.add_edge("transaction", "analysis_sync")

# 4. From sync, run goal and advice in parallel
builder.add_edge("analysis_sync", "goal")
builder.add_edge("analysis_sync", "advice")

# 5. Both goal and advice flow to planning sync
builder.add_edge("goal", "planning_sync")
builder.add_edge("advice", "planning_sync")

# 6. From planning sync to report
builder.add_edge("planning_sync", "report")

# 7. After report, run report_eval
builder.add_edge("report", "report_eval")

# 8. Report eval decides: if satisfied -> END, else -> back to report
def eval_decision(state):
    if hasattr(state, 'report_eval') and state.report_eval:
        eval_data = state.report_eval
        if isinstance(eval_data, dict):
            is_completed = eval_data.get("is_completed", False)
            overall_score = eval_data.get("overall_score", 0)
            
            print(f"\n📊 REPORT EVALUATION RESULTS:")
            print(f"   ✅ Completed: {is_completed}")
            print(f"   📈 Overall Score: {overall_score}")
            
            if is_completed:
                print("   🎉 Report approved! Ending workflow.")
                return "end"
            else:
                print("   🔄 Report needs improvement! Looping back to report generation...")
                feedback = eval_data.get("feedback", "No specific feedback")
                print(f"   💬 Feedback: {feedback}")
                return "report"
    
    print("   ⚠️  No evaluation data found. Ending workflow.")
    return "end"

builder.add_conditional_edges(
    "report_eval",
    eval_decision,
    {"end": END, "report": "report"}
)

# Compile
graph = builder.compile()
# dot_string = graph.get_graph().to_dot()
# with open("finance_graph.dot", "w") as f:
#     f.write(dot_string)

async def run_async():
    """Async version - use this for GUI integration"""
    input_state = {
        "user_data": {
            "age": 28,
            "occupation": "Software Engineer",
            "annual_income": 85000,
            "financial_goals": "Save for house down payment and build emergency fund",
            "target_amount": 50000,
            "timeline": "3 years",
            "risk_tolerance": "Moderate"
        }
    }

    print("🚀 Starting Financial Advisor Workflow...")
    print("📊 Workflow: Collector → [Behavior + Transaction] → [Goal + Advice] → Report → Eval")
    
    result = await graph.ainvoke(input_state)
    
    print("\n" + "="*60)
    print("🎯 WORKFLOW COMPLETED!")
    print("="*60)
    
    if hasattr(result, 'report') and result.report:
        print("📄 Final Report Generated ✅")
    
    if hasattr(result, 'report_eval') and result.report_eval:
        eval_data = result.report_eval
        if isinstance(eval_data, dict):
            print(f"📊 Final Evaluation: {eval_data.get('overall_score', 'N/A')}/10")
    
    return result

def run():
    """Synchronous wrapper for the async function"""
    import asyncio
    return asyncio.run(run_async())

def run_old():
    """Run the financial advisor graph with your desired workflow"""
    input_state = DeepResearchState(
        user_data={
            "age": 28,
            "occupation": "Software Engineer",
            "annual_income": 85000,
            "financial_goals": "Save for house down payment and build emergency fund",
            "target_amount": 50000,
            "timeline": "3 years",
            "risk_tolerance": "Moderate"
        }
    )

    print("🚀 Starting Financial Advisor Workflow...")
    print("📊 Workflow: Collector → [Behavior + Transaction] → [Goal + Advice] → Report → Eval")
    
    result = graph.invoke(input_state.dict())
    
    print("\n" + "="*60)
    print("🎯 WORKFLOW COMPLETED!")
    print("="*60)
    
    if result.get("report"):
        print("📄 Final Report Generated:")
        report_data = result["report"]
        if isinstance(report_data, dict) and "final_report" in report_data:
            print(result["report"]["final_report"])
        else:
            print("Report data:", report_data)
    
    if result.get("report_eval"):
        print("\n� Report Evaluation:")
        eval_data = result["report_eval"]
        if isinstance(eval_data, dict):
            print(f"✅ Completed: {eval_data.get('is_completed', 'Unknown')}")
            print(f"📈 Overall Score: {eval_data.get('overall_score', 'N/A')}")
            if "feedback" in eval_data:
                print(f"💬 Feedback: {eval_data['feedback']}")
    
    return result

if __name__ == "__main__":
    run()