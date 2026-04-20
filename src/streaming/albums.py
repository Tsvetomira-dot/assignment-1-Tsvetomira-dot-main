"""
albums.py
---------
Implement the Album class for collections of AlbumTrack objects.

Classes to implement:
  - Album
"""
from artists import Artist

class Album:
    def __init__(self, title: str, artist: 'Artist', release_year: int):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.tracks = []

    def add_Track(self, track):
        self.tracks.append(track)
        track.album = self
    
#    def duration_seconds(self):
#        return sum(duration for s in self.Track) ???
