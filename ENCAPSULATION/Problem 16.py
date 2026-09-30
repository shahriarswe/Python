class Playlist:
    def __init__(self):
        self.__songs = []

    def add_song(self, song):
        self.__songs.append(song)

    def get_songs(self):
        return tuple(self.__songs)  # returns an immutable copy

@register
def demo_16():
    pl = Playlist()
    pl.add_song("Song A")
    pl.add_song("Song B")
    print("16: songs =", pl.get_songs())

