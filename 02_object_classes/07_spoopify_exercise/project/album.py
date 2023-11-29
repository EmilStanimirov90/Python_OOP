from song import Song
class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.songs = songs
        self.published = False
        self.songs = []

    def add_song(self, song: Song):
        if song not in self.songs:
            self.songs.append(song)
