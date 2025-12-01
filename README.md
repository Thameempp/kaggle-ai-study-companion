# AI Study Companion - Multi-Agent Learning System

## 📖 Overview
An intelligent multi-agent system that provides personalized learning experiences by combining planning, research, and tutoring capabilities.

## 🎯 Problem Statement
Students often struggle with:
- Overwhelming amount of learning resources
- Lack of personalized learning paths
- Difficulty finding accurate, up-to-date information
- Need for interactive code examples

## 💡 Solution
A multi-agent AI system that:
1. **Plans** structured learning paths
2. **Researches** accurate information via Google Search
3. **Tutors** with personalized lessons and live code execution

## 🏗️ Architecture

### Multi-Agent System (3 Agents)
- **Planner Agent**: Breaks down topics into learning modules
- **Researcher Agent**: Gathers information using Google Search
- **Tutor Agent**: Creates personalized lessons with code examples

### Technologies Used
- Google ADK (Agent Development Kit)
- Gemini 2.0 Flash Exp
- Google Search Tool
- Code Execution Tool
- Session-based Memory Management

### 3 Core Concepts Implemented
✅ **1. Multi-Agent System** - Sequential agent orchestration  
✅ **2. Tools** - Google Search + Code Execution  
✅ **3. Memory** - Session management for learning progress

## 🚀 How to Run

### Prerequisites
- Python 3.9+
- Google AI Studio API Key ([Get one here](https://aistudio.google.com/app/apikey))

### Installation

```bash
# Clone repository
git clone https://github.com/yourusername/ai-study-companion.git
cd ai-study-companion

# Install dependencies
pip install -r requirements.txt

# Set API key
export GOOGLE_API_KEY='your_api_key_here'

# Run
python src/main.py
```

### Usage Example

```python
from src.main import run_study_companion

result = run_study_companion(
    user_query="Teach me about neural networks",
    session_id="user_456"
)
```

## 📁 Project Structure

```
ai-study-companion/
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── planner_agent.py      # Learning path planner
│   │   ├── researcher_agent.py   # Google Search integration
│   │   └── tutor_agent.py        # Personalized tutor
│   ├── tools/
│   │   ├── __init__.py
│   │   └── custom_tools.py       # Tool utilities
│   ├── memory/
│   │   ├── __init__.py
│   │   └── session_manager.py    # Session persistence
│   └── main.py                   # Main orchestration
├── requirements.txt
├── README.md
└── notebook.ipynb                # Kaggle notebook version
```

## 🔄 Agent Workflow

```
User Query
    ↓
🧠 Planner Agent
    ├─ Analyzes query
    ├─ Checks previous topics
    └─ Creates learning plan
    ↓
🔍 Researcher Agent
    ├─ Uses Google Search
    ├─ Gathers information
    └─ Verifies sources
    ↓
👨‍🏫 Tutor Agent
    ├─ Creates lesson
    ├─ Generates code examples
    └─ Provides exercises
    ↓
📖 Final Lesson + Memory Update
```

## 📊 Evaluation
- **Agent Communication**: Sequential workflow validated
- **Tool Usage**: Search queries and code execution logged
- **Memory Persistence**: Session data stored and retrieved
- **Output Quality**: Lessons reviewed for educational value

## 🎯 Track
**Agents for Good** - Educational accessibility and personalized learning

## 🔮 Future Improvements
- Add long-term memory with vector database
- Implement A2A protocol for peer learning
- Add observability dashboard
- Deploy as web service
- Multi-modal learning (images, videos)
- Adaptive difficulty based on performance
- Quiz generation and assessment

## 📝 Example Output

```
============================================================
📚 AI Study Companion - Processing Query
============================================================

🧠 Step 1: Planning learning path...
✅ Learning Plan Created

🔍 Step 2: Researching topic...
✅ Research Completed

👨‍🏫 Step 3: Creating personalized lesson...
✅ Lesson Created

============================================================
📖 FINAL LESSON
============================================================
[Comprehensive lesson content with code examples]
```

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License
MIT License

## 👥 Authors
Built for Kaggle's "Agents for Good" track

## 🙏 Acknowledgments
- Google ADK team for the Agent Development Kit
- Gemini API for powerful AI capabilities
- Kaggle for hosting the competition
