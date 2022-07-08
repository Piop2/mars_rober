import socket
from _thread import start_new_thread

from server_socket.client import Client

from config import parser


class ServerSocket:
    def __init__(self):
        # socket
        self.addr = ("", parser.server_port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.client = None

    def client_thread(self):
        while True:
            try:
                pass
            except:
                pass

    def listen(self):
        self.socket.listen()

        # wait for client connect
        while True:
            self.client = Client(*self.socket.accept())
            start_new_thread(self.client_thread, ())

    def run(self):
        self.socket.bind(self.addr)
