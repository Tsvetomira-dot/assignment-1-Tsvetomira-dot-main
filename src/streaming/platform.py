"""
platform.py
-----------
Implement the central StreamingPlatform class that orchestrates all domain entities
and provides query methods for analytics.

Classes to implement:
  - StreamingPlatform
"""
from datetime import datetime

class StreamingPlatform:
    def __init__(self, name: str):
        self.name = name
        self._catalogue = {}  
        self._users = {}     
        self._artists = {}  
        self._albums = {}   
        self._playlists = {} 
        self._sessions = []   

       """
        Calculates total duration from the global _sessions list 
        within the specified datetime range.
        """
    def total_listening_time_minutes(self, start: datetime, end: datetime) -> float:
        total_minutes = 0.0
        for session in self._sessions:
            if start <= session.timestamp <= end:
                total_minutes += session.duration_sec()        
        return total_minutes
