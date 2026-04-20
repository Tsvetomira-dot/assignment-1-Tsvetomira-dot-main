"""
playlists.py
------------
Implement playlist classes for organizing tracks.

Classes to implement:
  - Playlist
    - CollaborativePlaylist
"""

from tracks import Track


class Playlist:
    def __init__(self, playlist_id: str, name: str, owner):
        self.playlist_id = playlist_id
        self.name = name
        self.owner = owner
        self.tracks = []

    def add_track(self, track):
        self.tracks.append(track)

class CollaborativePlaylist(Playlist):
    def __init__(self, playlist_id: str, name: str, owner):
        super().__init__(playlist_id, name, owner)
        self.contributors = []

    def add_contributor(self, user) -> None:
        if user not in self.contributors:
            self.contributors.append(user)
