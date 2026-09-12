import random
from pathlib import Path

from config import MUSIC_PATH


class MusicHandler:
    def __init__(self):
        self.path_music = Path(MUSIC_PATH)
        self.list_music = []
        if self.path_music.is_dir():
            for file in self.path_music.iterdir():
                print(type(file))
                self.list_music.append(file)

    def random_music(self):
        print(self.list_music)
        random.shuffle(self.list_music)
        return self.list_music[0]
