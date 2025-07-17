# � AI-Powered Finance Manager

An intelligent financial management application that combines **Object-Oriented Programming** with **AI-powered insights** to help users track expenses, analyze spending patterns, and make informed financial decisions.

## 🎯 Overview

This project demonstrates advanced OOP concepts while solving real-world financial challenges through:
- **Smart Transaction Management** with bank statement imports
- **AI Financial Advisory** using LangGraph workflows
- **Intelligent Categorization** optimized for Indian financial context
- **Professional Reporting** with actionable insights

## ✨ Key Features

### 💳 **Financial Management**
- Add, update, and categorize transactions
- Import bank statements (PNB supported)
- Smart duplicate detection and filtering
- Export/import functionality

### 🤖 **AI Financial Advisor**
- **Goal Analysis** - Assess financial objectives and feasibility
- **Behavior Analysis** - Identify spending patterns and habits
- **Personalized Advice** - Tailored recommendations based on user profile
- **Professional Reports** - Comprehensive financial planning documents
- **Risk Assessment** - Evaluate financial health and suggest improvements

### 🖥️ **User Interface**
- Beautiful CLI with colored output and tables
- Streamlit web interface for interactive analysis
- Export reports and data visualization

## 🛠️ Tech Stack

**Core**: Python 3.13+, SQLite, Typer, Streamlit  
**AI**: LangGraph, LangChain, Groq, Pydantic  
**Tools**: Colorama, Tabulate, Python-dotenv

## 📁 Project Structure

```
Finance-Manager/
├── main.py                    # CLI entry point
├── basic_gui.py              # Streamlit web interface
├── pyproject.toml            # Project configuration
│
├── src/                      # Core application
│   ├── ai.py                # AI workflow coordinator
│   ├── financeManager.py    # Business logic
│   ├── config.py            # Configuration
│   │
│   ├── Ai/                  # AI Agent System
│   │   ├── graph.py         # LangGraph workflow
│   │   ├── nodes/           # AI processing nodes
│   │   ├── schemas/         # Data validation models
│   │   └── prompts/         # AI prompt templates
│   │
│   ├── database/            # Database management
│   ├── Banks/               # Bank statement parsers
│   └── Classifiers/         # Transaction categorization
│
└── data/                    # Database storage
    └── finance.db          # SQLite database
```

## � Quick Start

### Prerequisites
- Python 3.13+
- Groq API key (for AI features)

### Installation
```bash
# Clone repository
git clone https://github.com/siddhant385/Finance-Manager-main.git
cd Finance-Manager-main

# Install dependencies
pip install -e .

# Set up environment
cp .env.template .env
# Add your GROQ_API_KEY to .env
```

### Usage

**CLI Interface:**
```bash
# View financial summary
python main.py

# Add transaction
python main.py add "food" 250.50 "2024-01-15" "Lunch"

# Import bank statement
python main.py import-statement "statement.csv" "pnb"

# AI Financial Advisor
python -c "from src.ai import AI; ai = AI(); print(ai.advisor({'goal': 'Buy laptop'}))"
```

**Web Interface:**
```bash
streamlit run basic_gui.py
```

## 📊 Project Status

**✅ Completed:**
- Core financial management system
- AI-powered financial advisory with LangGraph
- Bank statement import (PNB)
- CLI and web interfaces
- Professional report generation

**🔄 In Progress:**
- Enhanced Streamlit dashboard
- Additional bank integrations

**🎯 Planned:**
- Memory system for AI conversations
- Advanced analytics and visualizations
- Multi-user support

## 🏗️ Architecture Highlights

This project showcases **Object-Oriented Programming** principles:
- **Strategy Pattern** for bank parsers and classifiers
- **Abstract Factory** for component creation
- **Template Method** for processing workflows
- **SOLID Principles** throughout the codebase

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.






