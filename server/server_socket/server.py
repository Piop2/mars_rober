import socket
from _thread import start_new_thread

from server_socket.client import Client
from server_socket.error import ClientDisconnected, ClientNotConnected, NoDataReceived

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
                # receive camera image only...
                _ = self.client.receive()
                
                # send controller key event
                k = self.app.input
                axis1 = k.app.axis1[0]
                axis2 = - k.app.axis2[1]
                motor1 = 0
                motor2 = 0
                if k.up:
                    motor1 = axis1
                    motor2 = axis1
                elif k.down:
                    motor1 = - axis1
                    motor2 = - axis1
                elif k.left:
                    motor1 = - axis2
                    motor2 = axis2
                elif k.right:
                    motor1 = axis2
                    motor2 = - axis2

                self.client.send(motor1, motor2)

            except (ClientDisconnected, NoDataReceived):
                self.client_disconn()
                print("disconnected")

    def listen(self):
        self.socket.listen()

        # wait for client connect
        while True:
            print("wait...")
            self.client_conn(self.socket.accept())
            start_new_thread(self.client_thread, ())
            print("connected")

    def run(self):
        self.socket.bind(self.addr)
        start_new_thread(self.listen, ())
