# AI Study Companion - Quick Start Guide

## 🚀 What You Have

A complete **multi-agent AI learning system** ready for Kaggle's "Agents for Good" track!

## 📦 Project Location
```
/Users/thameem/Desktop/kaggle/capstone project/ai-study-companion/
```

## ⚡ Quick Start

### Option 1: Run Demo (No API Key Needed)
```bash
cd "/Users/thameem/Desktop/kaggle/capstone project/ai-study-companion"
python3 demo.py
```

### Option 2: Run Full System (Requires API Key)
```bash
cd "/Users/thameem/Desktop/kaggle/capstone project/ai-study-companion"

# Install dependencies
pip install -r requirements.txt

# Set your Google AI Studio API key
export GOOGLE_API_KEY='your_api_key_here'

# Run the system
python3 src/main.py
```

### Option 3: Kaggle Submission
1. Open `notebook.ipynb` in Kaggle
2. Add your API key in Cell 2
3. Run all cells
4. Submit to "Agents for Good" track

## 🎯 What It Does

**User Query** → **Planner Agent** → **Researcher Agent** → **Tutor Agent** → **Personalized Lesson**

- **Planner**: Creates learning path
- **Researcher**: Gathers info via Google Search
- **Tutor**: Creates lesson with code examples
- **Memory**: Tracks your learning progress

## 📁 Key Files

| File | Purpose |
|------|---------|
| `src/main.py` | Main orchestration script |
| `notebook.ipynb` | Kaggle notebook version |
| `demo.py` | Demo without API key |
| `README.md` | Full documentation |
| `requirements.txt` | Dependencies |

## 🔑 Get API Key

Visit: https://aistudio.google.com/app/apikey

## ✅ Ready for Submission

All 3 core concepts implemented:
- ✅ Multi-Agent System (3 agents)
- ✅ Tools (Google Search + Code Execution)
- ✅ Memory (Session management)

Track: **Agents for Good** (Education-focused)

---

**Need help?** Check `README.md` for detailed documentation.
