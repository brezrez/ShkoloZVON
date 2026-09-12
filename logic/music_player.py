import pygame
from pathlib import Path

pygame.mixer.init()


class MusicPlayer:
    def __init__(self):
        self.is_running = True

    def play_music(self, name_music: str, time_playing: int = 60):
        pygame.mixer.music.load(name_music)
        pygame.mixer.music.play()
        if pygame.mixer.music.get_busy() and self.is_running:
            pygame.time.Clock().tick((10000000000 / time_playing) / 10000000000)
            pygame.mixer.music.stop()
        else:
            pygame.mixer.music.stop()
        self.is_running = True

    def stop(self):
        self.is_running = False
