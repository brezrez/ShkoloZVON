import ast, sqlite3
import os
import pickle
import socket
import threading
from pathlib import Path
from typing import Optional


# server = socket.socket()
# host = '0.0.0.0'
# port = 55555 # устанавливаем порт сервера
#
# server.bind((host, port))


class Server:
    def __init__(self, port: int = 55555):
        self.server = socket.socket()
        self.port = port
        self.server.bind('0.0.0.0', self.port)
        self.flow_server: Optional[threading.Thread] = None
        self.is_running = False

    def start(self):
        if self.is_running:
            return
        self.is_running = True
        self.flow_server = threading.Thread(target=self._run, daemon=True)
        self.flow_server.start()

    def _run(self):
        while self.is_running:
            self.server.listen(5)  # начинаем прослушивание входящих подключений
            con, addr = self.server.accept()  # принимаем клиент
            try:
                while self.is_running:
                    message = con.recv(400000000)  # сообщение для отправки клиенту
                    message = message.decode()
                    if message[0] == '1':
                        with open("vol.vbs", "w") as f:
                            if message[1] == "up":
                                f.write('set WshShell = CreateObject("WScript.Shell")\nWshShell.SendKeys chr(175)')
                            else:
                                f.write('set WshShell = CreateObject("WScript.Shell")\nWshShell.SendKeys chr(174)')

                        # Запускаем его через систему
                        os.system("cscript //nologo vol.vbs")
                        # Удаляем за собой
                        os.remove("vol.vbs")
                        break
            finally:
                pass

    def stop(self):
        self.is_running = False
