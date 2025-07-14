## 📌  Description / Idea

A **Professional Finance Management Application** designed specifically for **Indian users**.  
This project demonstrates **advanced Object-Oriented Programming concepts** while solving real-world financial tracking challenges.  
It provides comprehensive financial analysis with bank statement import, smart categorization, and future AI-powered insights.

> **Educational Purpose**: This project was developed as a comprehensive **OOP learning exercise**, showcasing inheritance, polymorphism, abstraction, and design patterns in a practical financial domain.

## 🎯 Project Status & Roadmap

### ✅ **Completed Features**
-  [x]  **Core FinanceManager System** - Complete CRUD operations with advanced filtering
-  [x]  **DatabaseManager** - Robust SQLite implementation with duplicate detection
-  [x]  **Multi-Bank Import System** - Extensible architecture supporting multiple banks (PNB implemented)
-  [x]  **Smart Transaction Classifier** - Rule-based categorization with configurable keywords
-  [x]  **Professional CLI Interface** - Beautiful Typer-based CLI with colored output and tables
-  [x]  **Export/Import Functionality** - CSV export and bank statement import

### 🚧 **In Development**
- [ ]  **LangGraph AI Agent** - Intelligent financial advisor with conversational interface
- [ ]  **Predictive Analytics** - Future expense forecasting and budget recommendations
- [ ]  **Interactive Dashboard** - Streamlit-based GUI with charts and visualizations

### 🎯 **Future Enhancements**
- [ ]  **FastAPI + React Web Interface** - Modern web application
- [ ]  **Notification System** - Email/SMS alerts and budget warnings
- [ ]  **Multi-user Support** - User authentication and data isolation
- [ ]  **Advanced AI Features** - Personalized financial advice and trend analysis

## 🛠️ Technical Stack & Dependencies

**Core Technologies:**
- Python 3.13+
- SQLite3 (built-in database)
- Typer (CLI framework)
- Colorama (colored terminal output)
- Tabulate (beautiful table formatting)

**Future Integrations:**
- LangGraph (AI agent framework)
- Streamlit (interactive GUI)
- FastAPI + React (web interface)
- OpenAI/Local LLMs (financial advice)

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

> **🏗️ Architecture Note**: The project follows **SOLID principles** with clean separation of concerns, making it easy to extend with new banks, classifiers, and AI features.


## ✨ **Current Features**

### 💰 **Financial Management**
- **Add/Update/Delete** transactions with tags, amounts, and dates
- **Smart Filtering** by date, month, or category
- **Comprehensive Summaries** with total expenses and category breakdowns
- **Duplicate Detection** prevents redundant entries

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

## 🚀 **Upcoming AI Features**

### 🤖 **LangGraph AI Agent**
- **Conversational Financial Advisor** for personalized guidance
- **Predictive Analytics** for future expense forecasting
- **Budget Recommendations** based on spending patterns
- **Natural Language Queries** ("How much did I spend on food this month?")

### 📊 **Advanced Analytics**
- **Trend Analysis** with visual representations
- **Anomaly Detection** for unusual spending patterns
- **Financial Goal Tracking** with progress monitoring
- **Smart Notifications** for budget limits and insights

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
```

### **Usage Examples**
```bash
# View financial summary (default command)
python main.py

# Add a new expense
python main.py add "food" 250.50 "2024-01-15"

# Import bank statement
python main.py import-statement "path/to/statement.csv" "pnb"

# View all transactions
python main.py view-all

# Filter by month
python main.py filter-month "2024-01"

# Export data
python main.py export "expenses.csv"
```

## 🔮 **Future Roadmap**

### **Phase 1: AI Integration (Current Focus)**
- LangGraph-based financial advisor
- Natural language processing for queries
- Predictive analytics and forecasting
- Streamlit interactive dashboard

### **Phase 2: Web Application**
- FastAPI backend with RESTful APIs
- React frontend with modern UI/UX
- Real-time data visualization
- Multi-user authentication

### **Phase 3: Advanced Features**
- Mobile application (Flutter/React Native)
- Integration with multiple Indian banks
- Advanced ML models for expense prediction
- Automated budget optimization






