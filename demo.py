"""
Demo script to test the AI Study Companion without API key
This script demonstrates the structure and flow without making actual API calls
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from agents.planner_agent import create_planner_agent
from agents.researcher_agent import create_researcher_agent
from agents.tutor_agent import create_tutor_agent
from memory.session_manager import SessionManager

def demo_agent_structure():
    """Demonstrate agent structure without API calls"""
    
    print("=" * 60)
    print("AI Study Companion - Structure Demo")
    print("=" * 60)
    print()
    
    # Mock client (not actually used in this demo)
    mock_client = None
    
    # Create agents
    print("🤖 Creating Agents...")
    
    # Note: These functions would normally require google-genai to be installed
    # For demo purposes, we're just showing the structure
    try:
        planner = create_planner_agent(mock_client)
        researcher = create_researcher_agent(mock_client)
        tutor = create_tutor_agent(mock_client)
        
        print(f"✅ {planner['name']}: {planner['role']}")
        print(f"✅ {researcher['name']}: {researcher['role']}")
        print(f"   - Tools: Google Search")
        print(f"✅ {tutor['name']}: {tutor['role']}")
        print(f"   - Tools: Code Execution")
    except Exception as e:
        print("⚠️  Note: google-genai package not installed")
        print("   Agent structure defined but requires API for full demo")
        print("   Install with: pip install google-genai")
        print()
        print("✅ planner_agent: learning_planner")
        print("✅ researcher_agent: information_researcher")
        print("   - Tools: Google Search")
        print("✅ tutor_agent: personalized_tutor")
        print("   - Tools: Code Execution")
    print()
    
    # Test session manager
    print("💾 Testing Session Manager...")
    session_manager = SessionManager(storage_path='./demo_sessions')
    
    # Create a demo session
    session_id = "demo_user_001"
    session = session_manager.get_session(session_id)
    print(f"✅ Created session: {session_id}")
    print(f"   - Level: {session['level']}")
    print(f"   - Topics covered: {session['topics_covered']}")
    print()
    
    # Simulate adding topics
    session['topics_covered'].append("Binary Search Trees")
    session['topics_covered'].append("Neural Networks")
    session['level'] = "intermediate"
    session_manager.save_session(session_id, session)
    print("✅ Updated session with topics")
    print()
    
    # Retrieve session
    updated_session = session_manager.get_session(session_id)
    print("📊 Session Data:")
    print(f"   - Session ID: {updated_session['session_id']}")
    print(f"   - Level: {updated_session['level']}")
    print(f"   - Topics: {', '.join(updated_session['topics_covered'])}")
    print(f"   - Created: {updated_session['created_at']}")
    print(f"   - Updated: {updated_session['updated_at']}")
    print()
    
    # Show workflow
    print("🔄 Multi-Agent Workflow:")
    print("   1. User Query → Planner Agent")
    print("      └─ Creates structured learning plan")
    print("   2. Learning Plan → Researcher Agent")
    print("      └─ Gathers info via Google Search")
    print("   3. Research Data → Tutor Agent")
    print("      └─ Creates lesson with code examples")
    print("   4. Final Lesson → User + Memory Update")
    print()
    
    print("=" * 60)
    print("✅ Demo Complete!")
    print("=" * 60)
    print()
    print("To run with actual API:")
    print("1. Set GOOGLE_API_KEY environment variable")
    print("2. Run: python src/main.py")
    print()

if __name__ == "__main__":
    demo_agent_structure()
