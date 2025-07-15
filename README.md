## 📌  Description / Idea

A **Professional AI-Powered Finance Management Application** designed specifically for **Indian users**.  
This project demonstrates **advanced Object-Oriented Programming concepts** while solving real-world financial tracking challenges.  
It provides comprehensive financial analysis with bank statement import, smart categorization, and **AI-powered financial advisory** using LangGraph.

> **Educational Purpose**: This project was developed as a comprehensive **OOP learning exercise**, showcasing inheritance, polymorphism, abstraction, and design patterns in a practical financial domain with **cutting-edge AI integration**.

## 🎯 Project Status & Roadmap

### ✅ **Completed Features (Phase 1 + Phase 2)**
-  [x]  **Core FinanceManager System** - Complete CRUD operations with advanced filtering
-  [x]  **DatabaseManager** - Robust SQLite implementation with duplicate detection
-  [x]  **Multi-Bank Import System** - Extensible architecture supporting multiple banks (PNB implemented)
-  [x]  **Smart Transaction Classifier** - Rule-based categorization with configurable keywords
-  [x]  **Professional CLI Interface** - Beautiful Typer-based CLI with colored output and tables
-  [x]  **Export/Import Functionality** - CSV export and bank statement import
-  [x]  **🤖 LangGraph AI Agent** - Complete agentic workflow with 5 specialized nodes
-  [x]  **🧠 Financial Analyzer** - Goal analysis, risk assessment, and feasibility evaluation
-  [x]  **📊 Goal Planner** - Inflation-adjusted financial planning with realistic timelines
-  [x]  **💡 Advice Generator** - Personalized financial advice based on user profile
-  [x]  **📑 Report Generator** - Professional markdown reports with actionable insights
-  [x]  **🔧 Pydantic Schemas** - Structured data validation for all AI responses
-  [x]  **🎯 Prompt Engineering** - Context-aware prompts for each financial scenario

### 🚧 **In Development (Phase 2 - 75% Complete)**
- [x]  **LangGraph AI Agent** - ✅ **COMPLETED** - Fully functional with all nodes
- [ ]  **Memory System** - ChromaDB for conversation persistence (25% remaining)
- [ ]  **Simple NLP Agent** - Fast Q&A for basic queries ("How much spent last month?")
- [ ]  **Personality Profiler** - Financial behavior analysis and spending patterns
- [ ]  **Interactive Dashboard** - Streamlit-based GUI with charts and visualizations

### 🎯 **Future Enhancements (Phase 3)**
- [ ]  **FastAPI + React Web Interface** - Modern web application
- [ ]  **Notification System** - Email/SMS alerts and budget warnings
- [ ]  **Multi-user Support** - User authentication and data isolation
- [ ]  **Advanced ML Models** - Predictive analytics and anomaly detection

## 🛠️ Technical Stack & Dependencies

**Core Technologies:**
- Python 3.13+
- SQLite3 (built-in database)
- Typer (CLI framework)
- Colorama (colored terminal output)
- Tabulate (beautiful table formatting)

**AI & Machine Learning:**
- LangGraph (AI agent orchestration)
- LangChain (LLM integration framework)
- Groq (High-performance LLM inference)
- Pydantic (Data validation and schemas)
- Python-dotenv (Environment management)

**Future Integrations:**
- ChromaDB (Vector database for memory)
- Streamlit (Interactive GUI)
- FastAPI + React (Web interface)
- Plotly/Matplotlib (Data visualization)

## 📁 Project Architecture

```
Finance-Manager/
│
├── main.py                     # CLI entry point with Typer commands
├── pyproject.toml             # Modern Python project configuration
├── uv.lock                    # Dependency lock file
│
├── src/                       # Core application logic
│   ├── __init__.py
│   ├── config.py              # Global configuration and constants
│   ├── financeManager.py      # Main business logic coordinator
│   ├── databaseManager.py     # SQLite database operations
│   ├── importer.py            # Bank statement processing orchestrator
│   │
│   ├── ai/                    # 🤖 AI Agent System (LangGraph Implementation)
│   │   ├── graph.py           # LangGraph workflow orchestration
│   │   ├── prompts.py         # AI prompt templates and engineering
│   │   │
│   │   ├── nodes/             # AI Agent Nodes (Modular Processing)
│   │   │   ├── collector.py   # Financial data collection and structuring
│   │   │   ├── analyzer.py    # Goal analysis and risk assessment
│   │   │   ├── goalPlanner.py # Financial goal planning with inflation
│   │   │   ├── adviceGenerator.py # Personalized financial advice
│   │   │   └── summarizer.py  # Professional report generation
│   │   │
│   │   ├── schemas/           # Pydantic data models for AI responses
│   │   │   ├── analyzer.py    # Analysis result structure
│   │   │   ├── goalPlanner.py # Goal planning data model
│   │   │   └── advice.py      # Advice response structure
│   │   │
│   │   ├── utils/             # AI utility functions
│   │   │   └── json_utils.py  # JSON extraction and validation
│   │   │
│   │   ├── llm_config/        # LLM configuration (In Development)
│   │   │   ├── base.py        # Base LLM configuration
│   │   │   └── selectory.py   # Model selection logic
│   │   │
│   │   └── tools/             # AI tools and integrations (Future)
│   │
│   ├── Banks/                 # Bank-specific parsers (Strategy Pattern)
│   │   ├── __init__.py
│   │   ├── base.py           # Abstract base class for all banks
│   │   └── pnb.py            # Punjab National Bank implementation
│   │
│   └── Classifiers/           # Transaction categorization (Strategy Pattern)
│       ├── base.py           # Abstract classifier interface
│       ├── rule_based.py     # Keyword-based classification
│       └── ai_based.py       # Future: LLM-based classification
│
├── data/                      # Persistent storage
│   └── finance.db            # SQLite database (auto-created)
│
└── README.md                 # Project documentation
```

> **🏗️ Architecture Note**: The project follows **SOLID principles** with clean separation of concerns, making it easy to extend with new banks, classifiers, and AI features. The **AI module** uses modular LangGraph nodes for scalable financial intelligence.


## ✨ **Current Features**

### 💰 **Core Financial Management**
- **Add/Update/Delete** transactions with tags, amounts, and dates
- **Smart Filtering** by date, month, or category
- **Comprehensive Summaries** with total expenses and category breakdowns
- **Duplicate Detection** prevents redundant entries
- **Savings Calculation** and trend analysis

### 🏦 **Bank Integration**
- **Multi-Bank Support** with extensible architecture
- **Punjab National Bank (PNB)** CSV statement import
- **Automatic Transaction Parsing** with data sanitization
- **Smart Date & Amount Standardization**

### 🏷️ **Intelligent Categorization**
- **Rule-Based Classification** using configurable keywords
- **Indian Context Aware** (Zomato, Swiggy, Myntra, etc.)
- **Customizable Categories** for personalized tracking
- **Unknown Category Handling** for unmatched transactions

### 🖥️ **Professional CLI Interface**
- **Colorful Output** with beautiful table formatting
- **Interactive Commands** for all operations
- **Export to CSV** functionality
- **Import Bank Statements** with single command

### 🤖 **AI-Powered Financial Advisory (NEW!)**
- **LangGraph Agent Workflow** with 5 specialized nodes
- **Goal Analysis** - Assess financial goals and feasibility
- **Risk Assessment** - Evaluate spending patterns and financial health
- **Inflation-Adjusted Planning** - Realistic goal timelines with inflation
- **Personalized Advice** - Tailored recommendations based on user profile
- **Professional Reports** - Markdown-formatted financial planning reports
- **Smart Validation** - Pydantic schemas ensure data integrity

## 🚀 **AI Agent Capabilities**

### 🧠 **Financial Intelligence**
- **Pattern Recognition** - Identify spending habits and financial behaviors
- **Feasibility Analysis** - Realistic goal assessment based on current finances
- **Budget Optimization** - Suggest expense reductions and savings strategies
- **Risk Evaluation** - Assess financial risks and provide mitigation advice

### 📊 **Advanced Analytics**
- **Trend Analysis** - Monthly income/expense patterns
- **Anomaly Detection** - Identify unusual spending patterns
- **Goal Tracking** - Monitor progress toward financial objectives
- **Predictive Insights** - Future financial planning recommendations

## 🎓 **Object-Oriented Programming Showcase**

This project serves as a comprehensive demonstration of **advanced OOP concepts**:

### 🏗️ **Design Patterns Implemented**
- **Abstract Factory Pattern** - Bank and Classifier creation
- **Strategy Pattern** - Multiple bank parsers and classification algorithms
- **Template Method Pattern** - Base classes defining processing workflows
- **Dependency Injection** - Configurable components and keyword mappings

### 🔧 **OOP Principles Demonstrated**
- **Abstraction** - Abstract base classes (`Base`, `BaseClassifier`)
- **Inheritance** - Bank-specific implementations extending base classes
- **Encapsulation** - Private methods and properties with controlled access
- **Polymorphism** - Unified interfaces for different banks and classifiers

### 📐 **SOLID Principles**
- **Single Responsibility** - Each class has one clear purpose
- **Open/Closed** - Easy to extend with new banks without modifying existing code
- **Liskov Substitution** - All implementations are interchangeable
- **Interface Segregation** - Focused, minimal interfaces
- **Dependency Inversion** - High-level modules don't depend on low-level details

## 🚀 **Quick Start**

### **Prerequisites**
```bash
# Python 3.13+ required
python --version

# Install uv (recommended) or use pip
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### **Installation**
```bash
# Clone the repository
git clone https://github.com/siddhant385/Finance-Manager-main.git
cd Finance-Manager-main

# Install dependencies
uv sync
# or with pip: pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your GROQ_API_KEY in .env file
```

### **Basic Usage Examples**
```bash
# View financial summary (default command)
python main.py

# Add a new expense
python main.py add "food" 250.50 "2024-01-15" "Lunch at restaurant"

# Import bank statement
python main.py import-statement "path/to/statement.csv" "pnb"

# View all transactions
python main.py view-all

# Filter by month
python main.py filter-month "2024-01"

# Export data
python main.py export "expenses.csv"
```

### **🤖 AI Agent Usage**
```bash
# Run the AI Financial Advisor
python -c "from src.ai.graph import run; run()"

# The AI will analyze your financial data and provide:
# - Goal feasibility analysis
# - Personalized financial advice
# - Budget optimization suggestions
# - Professional financial report
```

## 🔮 **Future Roadmap**

### **Phase 2: AI Enhancement (75% Complete)**
- [x] LangGraph-based financial advisor - **COMPLETED**
- [x] Structured AI responses with Pydantic schemas - **COMPLETED**
- [x] Professional financial report generation - **COMPLETED**
- [ ] Memory system with ChromaDB for conversation persistence
- [ ] Simple NLP agent for quick queries ("How much spent on food?")
- [ ] Personality profiler for financial behavior analysis

### **Phase 3: User Interface & Visualization**
- [ ] Streamlit interactive dashboard with charts
- [ ] Real-time data visualization with Plotly
- [ ] Financial goal tracking interface
- [ ] Budget management dashboard

### **Phase 4: Web Application**
- [ ] FastAPI backend with RESTful APIs
- [ ] React frontend with modern UI/UX
- [ ] Real-time notifications and alerts
- [ ] Multi-user authentication system

### **Phase 5: Advanced Features**
- [ ] Mobile application (Flutter/React Native)
- [ ] Integration with multiple Indian banks
- [ ] Advanced ML models for expense prediction
- [ ] Automated budget optimization
- [ ] Investment portfolio tracking






