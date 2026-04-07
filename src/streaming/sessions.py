"""
sessions.py
-----------
Implement the ListeningSession class for recording listening events.

Classes to implement:
  - ListeningSession
"""
from datetime import datetime

class ListeningSession:
    def __init__(self, user, track, duration_sec: int):
        self.user = user
        self.track = track
        self.duration_sec = duration_sec

    def duration(self) -> float:
        return self.duration_sec / 60.0