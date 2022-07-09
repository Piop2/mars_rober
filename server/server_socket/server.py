import socket
from _thread import start_new_thread

from server_socket.client import Client
from server_socket.error import ClientNotConnected, NoDataReceived

from config import parser


class ServerSocket:
    def __init__(self, app):
        self.app = app

        # socket
        self.addr = ("", parser.server_port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.client = None

    @property
    def client_camera_img(self):
        if self.client is None:
            raise NoDataReceived()
        if self.client.camera_img is None:
            raise ClientNotConnected()
        return self.client.camera_img

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
                # 아직 클라이언트한테 받는 데이터는 이미지 밖에 없습니다
                _ = self.client.receive()
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
