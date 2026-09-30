class Playlist38:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]

@register
def demo_38():
    pl = Playlist38(["Song A", "Song B", "Song C"])
    print("38: length =", len(pl), "| second song =", pl[1])
