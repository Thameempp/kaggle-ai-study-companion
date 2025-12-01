import json
import os
from datetime import datetime

class SessionManager:
    """
    Manages user learning sessions and memory persistence.
    Implements short-term memory for the agent system.
    """
    
    def __init__(self, storage_path='./sessions'):
        self.storage_path = storage_path
        os.makedirs(storage_path, exist_ok=True)
    
    def get_session(self, session_id: str) -> dict:
        """Load existing session or create new one"""
        session_file = os.path.join(self.storage_path, f'{session_id}.json')
        
        if os.path.exists(session_file):
            with open(session_file, 'r') as f:
                return json.load(f)
        
        # New session
        return {
            'session_id': session_id,
            'created_at': datetime.now().isoformat(),
            'topics_covered': [],
            'level': 'beginner',
            'interactions': []
        }
    
    def save_session(self, session_id: str, session_data: dict):
        """Persist session data"""
        session_data['updated_at'] = datetime.now().isoformat()
        session_file = os.path.join(self.storage_path, f'{session_id}.json')
        
        with open(session_file, 'w') as f:
            json.dump(session_data, f, indent=2)
    
    def get_learning_history(self, session_id: str) -> list:
        """Get all topics covered by user"""
        session = self.get_session(session_id)
        return session.get('topics_covered', [])
    
    def update_level(self, session_id: str, new_level: str):
        """Update user's learning level"""
        session = self.get_session(session_id)
        session['level'] = new_level
        self.save_session(session_id, session)
    
    def add_interaction(self, session_id: str, query: str, response: str):
        """Record an interaction"""
        session = self.get_session(session_id)
        interaction = {
            'timestamp': datetime.now().isoformat(),
            'query': query,
            'response_preview': response[:200] + '...' if len(response) > 200 else response
        }
        session['interactions'] = session.get('interactions', []) + [interaction]
        self.save_session(session_id, session)
