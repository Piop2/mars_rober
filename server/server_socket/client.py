import server_socket.message
from utils.image import decode_image
from server_socket.error import ClinetDisconnected

class Client:
    def __init__(self, socket, addr):
        self.addr = addr
        self.socket = socket

        self.camera_img = None

    def send(self, up, down, left, right):
        data = {'event': {'up': up, 'down': down, 'left': left, 'right': right}}
        server_socket.message.send(self.socket, data)

    def receive(self):
        data = server_socket.message.receive(self.socket)

        # no received data -> raise error to disconnect the client
        if not data:
            raise ClinetDisconnected()
        
        # client camera img
        img = data['camera']['bytes']
        if img is not None:
            self.camera_img = decode_image(img)
        else:
            self.camera_img = None
        
        return data
