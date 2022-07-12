import socket
from _thread import start_new_thread

from client_socket.message import send, receive
from client_socket.error import *

from config import parser


class ClientSocket:
    def __init__(self, rover):
        self.rover = rover

        # socket
        self.addr = (parser.server_ip, parser.server_port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)

    def server_thread(self):
        while True:
            try:
                data = receive(self.socket)
                motor1 = data['motor1']
                motor2 = data['motor2']

                send(self.socket, {})
            except ConnectionError:
                pass

    def connect(self):
        print('CONNECTING..')
        self.socket.connect(self.addr)
        print('CONNECTED!')
        return

    def run(self):
        self.connect()
        start_new_thread(self.server_thread, ())
        return
