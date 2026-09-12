import datetime
import threading
import time
from typing import Optional, Callable


class TimerMusic:
    def __init__(self, time_music_callback: Callable, args: list,
                 list_time_music: list = ["9:15", "10:10", "11:10", "12:05", "13:10", "22:40", "14:43", "12:20",'14:35']):
        self.list_time_music = list_time_music
        self.thread_music: Optional[threading.Thread] = None
        self.is_running = False
        self.thread_time: Optional[threading.Thread] = None
        self._stop_event = threading.Event()
        self.time_playing = 60
        self.time_music_callback = time_music_callback
        self.args = args

    def start(self):
        if self.is_running:
            return

        self.is_running = True
        self._stop_event.clear()
        self.thread_time = threading.Thread(target=self._run, daemon=True)
        self.thread_time.start()

    def _run(self):
        while self.is_running:
            if self._stop_event.is_set():
                break

            time.sleep(5)

            timer = f"{datetime.datetime.now().strftime('%H:%M')}"
            for i in self.list_time_music:
                if i == timer:
                    if self.time_music_callback:
                        try:
                            self.time_music_callback(self.args[0], self.args[1])
                            time.sleep(self.time_playing)
                        except Exception as e:
                            print(e)

    def stop(self):
        """Останавливает таймер"""
        self.is_running = False
        self._stop_event.set()
