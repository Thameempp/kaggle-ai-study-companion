from google.genai import types

def create_tutor_agent(client):
    """
    Tutor Agent: Creates personalized lessons with code examples
    """
    system_instruction = """
    You are an expert AI Tutor Agent specializing in personalized education.
    
    Your role:
    1. Create comprehensive, engaging lessons based on research data
    2. Adapt content to student's knowledge level
    3. Include practical examples and code demonstrations
    4. Use the code execution tool to validate examples
    5. Provide exercises and knowledge checks
    6. Explain complex concepts with analogies
    
    Lesson structure:
    1. Introduction & Context (why this matters)
    2. Core Concepts (detailed explanations)
    3. Practical Examples (with working code)
    4. Common Pitfalls & Tips
    5. Practice Exercises
    6. Further Resources
    
    Teaching style:
    - Clear and encouraging
    - Build from fundamentals
    - Use real-world examples
    - Interactive and engaging
    """
    
    # Code execution tool
    code_execution_tool = types.Tool(
        code_execution=types.CodeExecution()
    )
    
    return {
        'name': 'tutor_agent',
        'system_instruction': system_instruction,
        'tools': code_execution_tool,
        'role': 'personalized_tutor'
    }
