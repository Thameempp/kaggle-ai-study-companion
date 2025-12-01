# AI Study Companion – Multi-Agent Learning System

## Overview

AI Study Companion is an intelligent multi-agent system designed to deliver personalized learning experiences by combining planning, research, and tutoring capabilities. It is built to simplify the learning process for students by organizing content, retrieving accurate information, and generating interactive lessons with executable code.

## Problem Statement

Students frequently face challenges such as:

* Overwhelming amounts of online learning resources
* Lack of personalized or structured learning paths
* Difficulty finding accurate and up-to-date information
* Limited access to interactive explanations and code examples

## Solution

This project introduces a multi-agent AI system that:

1. Plans structured learning paths based on user queries
2. Researches reliable information using Google Search
3. Generates personalized lessons, explanations, and executable code

## System Architecture

### Multi-Agent Design

The system uses a chain-of-agents workflow consisting of:

* **Planner Agent**
  Breaks down the user query into structured modules and learning steps.

* **Researcher Agent**
  Fetches accurate information using Google Search and validates findings.

* **Tutor Agent**
  Creates personalized lessons, explanations, and code examples.

### Technologies Used

* Google ADK (Agent Development Kit)
* Gemini 2.0 Flash Exp
* Google Search Tool
* Code Execution Tool
* Session-based Memory Manager

### Key Concepts Implemented

1. Multi-agent sequential orchestration
2. Integrated tool usage (search + code execution)
3. Session memory persistence

## How to Run

### Prerequisites

* Python 3.9 or higher
* Google AI Studio API Key (available at: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey))

### Installation

```bash
# Clone repository
git clone https://github.com/yourusername/ai-study-companion.git
cd ai-study-companion

# Install dependencies
pip install -r requirements.txt

# Set API key
export GOOGLE_API_KEY='your_api_key_here'

# Run the main program
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

## Project Structure

```
ai-study-companion/
├── src/
│   ├── agents/
│   │   ├── planner_agent.py       # Learning path planner
│   │   ├── researcher_agent.py    # Google Search integration
│   │   └── tutor_agent.py         # Personalized tutor
│   ├── tools/
│   │   └── custom_tools.py        # Tool utilities
│   ├── memory/
│   │   └── session_manager.py     # Session persistence
│   └── main.py                    # Main orchestration
├── requirements.txt
├── README.md
└── notebook.ipynb                 # Kaggle notebook version
```

## Agent Workflow

```
User Query
    ↓
Planner Agent
    - Analyzes query
    - Checks previous progress
    - Generates a structured learning plan
    ↓
Researcher Agent
    - Uses Google Search
    - Collects and validates information
    ↓
Tutor Agent
    - Creates detailed lessons
    - Generates code samples
    - Provides practice exercises
    ↓
Final Output + Memory Update
```

## Evaluation

* Verified communication flow across agents
* Tool usage logged and validated (search + code execution)
* Memory persistence across sessions tested
* Output quality evaluated for clarity and educational value

## Track

This project is submitted under the **Agents for Good** track, focusing on improving education accessibility and personalized learning.

## Future Improvements

* Long-term memory using a vector database
* A2A protocol for agent-to-agent collaboration
* Observability and monitoring dashboard
* Deployment as a production-grade web service
* Multi-modal learning with images and videos
* Adaptive difficulty levels based on learner performance
* Automated quiz generation and assessments

## Example Output

```

AI Study Companion - Processing Query
--------

Step 1: Planning learning path...
Learning Plan Created

Step 2: Researching topic...
Research Completed

Step 3: Creating personalized lesson...
Lesson Created


FINAL LESSON
--------
[Comprehensive lesson with explanations and code examples]
```

## Contributing

Contributions are welcome. Please submit a Pull Request if you would like to contribute improvements or new features.

## License

This project is released under the MIT License.

## Authors

Developed for the Kaggle "Agents for Good" competition track.

## Acknowledgments

* Google ADK team for the Agent Development Kit
* Gemini API for AI model capabilities
* Kaggle for providing the competition environment
