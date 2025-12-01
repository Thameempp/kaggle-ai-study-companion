"""Custom tools and utilities for AI Study Companion"""

from google.genai import types


def get_google_search_tool():
    """Returns configured Google Search tool"""
    return types.Tool(
        google_search=types.GoogleSearch()
    )


def get_code_execution_tool():
    """Returns configured Code Execution tool"""
    return types.Tool(
        code_execution=types.CodeExecution()
    )


def parse_tool_response(response):
    """
    Parse and extract useful information from tool responses
    
    Args:
        response: The response object from Gemini API
        
    Returns:
        str: Extracted text content
    """
    if hasattr(response, 'text'):
        return response.text
    elif hasattr(response, 'parts'):
        # Handle multi-part responses
        text_parts = []
        for part in response.parts:
            if hasattr(part, 'text'):
                text_parts.append(part.text)
        return '\n'.join(text_parts)
    else:
        return str(response)


def format_agent_output(agent_name: str, output: str, max_preview: int = 200) -> str:
    """
    Format agent output for display
    
    Args:
        agent_name: Name of the agent
        output: Output text
        max_preview: Maximum characters for preview
        
    Returns:
        str: Formatted output
    """
    preview = output[:max_preview] + '...' if len(output) > max_preview else output
    return f"[{agent_name}] {preview}"


__all__ = [
    'get_google_search_tool',
    'get_code_execution_tool', 
    'parse_tool_response',
    'format_agent_output'
]
