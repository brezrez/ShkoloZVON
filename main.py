from logic.timer import TimerMusic
from logic.music_player import MusicPlayer
from data.music import MusicHandler


tim = TimerMusic(MusicPlayer().play_music, [MusicHandler().random_music(), 60])
tim.start()

while True:
    pass



