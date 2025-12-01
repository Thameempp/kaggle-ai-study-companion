import os
from google import genai
from google.genai import types
from agents.planner_agent import create_planner_agent
from agents.researcher_agent import create_researcher_agent
from agents.tutor_agent import create_tutor_agent
from memory.session_manager import SessionManager

# Initialize Gemini client
client = genai.Client(api_key=os.environ.get('GOOGLE_API_KEY'))

# Initialize session manager (Memory)
session_manager = SessionManager()

def run_study_companion(user_query: str, session_id: str = "default"):
    """
    Main multi-agent orchestration function.
    Flow: User Query → Planner → Researcher → Tutor → Response
    """
    
    # Load session memory
    session_data = session_manager.get_session(session_id)
    
    print(f"\n{'='*60}")
    print(f"📚 AI Study Companion - Processing Query")
    print(f"{'='*60}\n")
    
    # Step 1: Planner Agent - Breaks down learning goal
    print("🧠 Step 1: Planning learning path...")
    planner_agent = create_planner_agent(client)
    
    planner_context = f"""
    User Query: {user_query}
    Previous Topics Covered: {session_data.get('topics_covered', [])}
    Current Level: {session_data.get('level', 'beginner')}
    """
    
    planner_response = client.models.generate_content(
        model='gemini-2.0-flash-exp',
        contents=planner_context,
        config=types.GenerateContentConfig(
            system_instruction=planner_agent['system_instruction'],
            temperature=0.7
        )
    )
    
    learning_plan = planner_response.text
    print(f"✅ Learning Plan Created:\n{learning_plan[:200]}...\n")
    
    # Step 2: Researcher Agent - Gathers information using search
    print("🔍 Step 2: Researching topic...")
    researcher_agent = create_researcher_agent(client)
    
    research_response = client.models.generate_content(
        model='gemini-2.0-flash-exp',
        contents=f"Research this topic thoroughly: {user_query}",
        config=types.GenerateContentConfig(
            system_instruction=researcher_agent['system_instruction'],
            tools=[researcher_agent['tools']],
            temperature=0.5
        )
    )
    
    research_data = research_response.text
    print(f"✅ Research Completed\n")
    
    # Step 3: Tutor Agent - Creates personalized lesson
    print("👨‍🏫 Step 3: Creating personalized lesson...")
    tutor_agent = create_tutor_agent(client)
    
    tutor_context = f"""
    Learning Plan: {learning_plan}
    Research Data: {research_data}
    Student Level: {session_data.get('level', 'beginner')}
    Previous Knowledge: {session_data.get('topics_covered', [])}
    
    Create a comprehensive lesson for: {user_query}
    """
    
    tutor_response = client.models.generate_content(
        model='gemini-2.0-flash-exp',
        contents=tutor_context,
        config=types.GenerateContentConfig(
            system_instruction=tutor_agent['system_instruction'],
            tools=[tutor_agent['tools']],  # Code execution for examples
            temperature=0.8
        )
    )
    
    final_lesson = tutor_response.text
    print(f"✅ Lesson Created\n")
    
    # Update session memory
    session_data['topics_covered'] = session_data.get('topics_covered', []) + [user_query]
    session_data['last_query'] = user_query
    session_manager.save_session(session_id, session_data)
    
    print(f"\n{'='*60}")
    print(f"📖 FINAL LESSON")
    print(f"{'='*60}\n")
    print(final_lesson)
    
    return {
        'plan': learning_plan,
        'research': research_data,
        'lesson': final_lesson,
        'session_id': session_id
    }

# Example usage
if __name__ == "__main__":
    result = run_study_companion(
        user_query="Explain binary search trees with code examples",
        session_id="user_123"
    )
