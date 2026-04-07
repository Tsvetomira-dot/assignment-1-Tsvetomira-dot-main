"""
tracks.py
---------
Implement the class hierarchy for all playable content on the platform.

Classes to implement:
  - Track (abstract base class)
    - Song
      - SingleRelease
      - AlbumTrack
    - Podcast
      - InterviewEpisode
      - NarrativeEpisode
    - AudiobookTrack
"""

from streaming.artists import Artist

class Track:
    def __init__(self, track_id: str, title: str, duration: float):
        self.track_id = track_id
        self.title = title
        self.duration = duration

class Song(Track):
    def __init__(self, track_id: str, title: str, duration: int, artist: 'Artist'):
        super().__init__(track_id, title, duration)
        self.artist = artist

class SingleRelease(Song):
    def __init__(self, track_id: str, title: str, duration: int, artist: 'Artist'):
        super().__init__(track_id, title, duration, artist)

class AlbumTrack(Song):
    def __init__(self, track_id: str, title: str, duration: int, artist: 'Artist'):
        super().__init__(track_id, title, duration, artist)

#--------------------------------------------------------------------

class Podcast(Track):
    def __init__(self, track_id: str, title: str, duration: int):
        super().__init__(track_id, title, duration)

class InterviewEpisode(Podcast):
    def __init__(self, track_id: str, title: str, duration:int):
        super().__init__(track_id, title, duration)

class NarrativeEpisode(Podcast):
    def __init__(self, track_id: str, title: str, duration: int):
        super().__init__(track_id, title, duration)

class AudiobookTrack(Track):
    def __init__(self, track_id: str, title: str, duration:int):
        super().__init__(track_id, title, duration)