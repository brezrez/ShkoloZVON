import random
from pathlib import Path

from config import MUSIC_PATH


class MusicHandler:
    def __init__(self):
        self.path_music = self.path_music = Path(__file__).parent / MUSIC_PATH
        print(self.path_music)
        self.list_music = []
        print(self.path_music.is_dir())
        if self.path_music.is_dir():
            for file in self.path_music.iterdir():
                print(type(file))
                self.list_music.append(file)

    def random_music(self):
        print(self.list_music)
        random.shuffle(self.list_music)
        return self.list_music[0]
