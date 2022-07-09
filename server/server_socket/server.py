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

    @property
    def is_client_conn(self):
        if self.client is None:
            return False
        return True

    def client_disconn(self):
        self.client = None
        return

    def client_conn(self, socket_data):
        self.client = Client(*socket_data)
        return

    def client_thread(self):
        while True:
            try:
                data = self.client.receive()
                # 데이터 처리부분 코드 써주세요
            except:
                self.client_disconn()

    def listen(self):
        self.socket.listen()

        # wait for client connect
        while True:
            self.client_conn(self.socket.accept())
            start_new_thread(self.client_thread, ())

    def run(self):
        self.socket.bind(self.addr)
