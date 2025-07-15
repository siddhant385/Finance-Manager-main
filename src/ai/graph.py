from .nodes.collector import CollectorNode
from .nodes.analyzer import AnalyzerNode
from .nodes.goalPlanner import GoalPlannerNode
from .nodes.adviceGenerator import AdviceGeneratorNode
from .nodes.summarizer import SummarizerNode


from langgraph.graph import StateGraph, END, START
from langgraph.types import Send
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Optional, Dict


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

# Assume `llm` is already initialized (ChatGroq / OpenAI etc.)

class FinancialAdvisorState(Dict):
    user_answers: Optional[Dict] = None
    collector_data: Optional[Dict] = None
    analysis_result: Optional[Dict] = None
    goal_planner_result: Optional[Dict] = None
    final_advice: Optional[Dict] = None
    final_report_markdown: Optional[str] = None



collector_node = CollectorNode()
analyzer_node = AnalyzerNode(llm)
goal_planner_node = GoalPlannerNode(llm)
advice_generator_node = AdviceGeneratorNode(llm)
summarizer_node = SummarizerNode(llm)


builder = StateGraph(FinancialAdvisorState)

builder.add_node("collector", collector_node)
builder.add_node("analyzer", analyzer_node)
builder.add_node("goal_planner", goal_planner_node)
builder.add_node("advice_generator", advice_generator_node)
builder.add_node("summarizer", summarizer_node)

# Add edges (flow of data)
builder.set_entry_point("collector")
builder.add_edge("collector", "analyzer")
builder.add_edge("analyzer", "goal_planner")
builder.add_edge("goal_planner", "advice_generator")
builder.add_edge("advice_generator", "summarizer")

# Define final state
builder.set_finish_point("summarizer")

# Compile
graph = builder.compile()


def run():
    input_state = {
        "user_answers": {
            "goal": "I want to save money for my future studies and financial statbility",
            "risk_question": "I will take calculated risks to achieve my financial goals",
            "kuch_important_question": "I am committed to making informed financial decisions",
        }
    }

    result = graph.invoke(input_state)
    print("\n📄 Final Report Markdown:\n", result["final_report_markdown"])
