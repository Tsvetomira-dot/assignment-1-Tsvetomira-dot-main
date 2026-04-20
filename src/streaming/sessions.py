"""
sessions.py
-----------
Implement the ListeningSession class for recording listening events.

Classes to implement:
  - ListeningSession
"""
from datetime import datetime

class ListeningSession:
    def __init__(self, user, track, timestamp: datetime, duration_sec: int):
        self.session_id = session_id
        self.user = user
        self.track = track
        self.timestamp = timestamp
        self.duration_sec = duration_sec

    def duration(self) -> float:
        return self.duration_sec / 60.0
