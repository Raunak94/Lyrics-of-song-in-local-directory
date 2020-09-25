import os
from pygame import mixer
import taglib
import azapi


class Music:
    songs = ["x"]
    for i in os.listdir():
        if i.endswith(".mp3"):
            songs.append(i)

    def music_play(self):
        for i in range(1, len(Music.songs)):
            print(str(i) + ":" + Music.songs[i])
        self.n = input("Enter Song Number to play: ")
        mixer.init()
        mixer.music.load(Music.songs[int(self.n)])
        mixer.music.play()

    def stop(self):
        mixer.music.stop()

    def resume(self):
        mixer.music.unpause()

    def pause(self):
        mixer.music.pause()

    def lyric(self):
        data = taglib.File(Music.songs[int(self.n)])
        API = azapi.AZlyrics('google', accuracy=0.5)
        API.artist = data.tags["ALBUMARTIST"][0]
        API.title = data.tags["TITLE"][0]
        API.getLyrics(save=False)
        print(API.lyrics)


mus = Music()

while True:
    print("Press 's' to select a song")
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to stop the song")
    print("Press 'l' to get lyrics of song")

    query = input(" ").lower()

    if query == 'p':
        mus.pause()
    elif query == 'r':
        mus.resume()
    elif query == 'e':
        mus.stop()
        break
    elif query == 's':
        mus.music_play()
    elif query == 'l':
        mus.lyric()
    else:
        print("WRONG INPUT.... TRY AGAIN")
        continue
