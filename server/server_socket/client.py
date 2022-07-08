import server_socket.message


class Client:
    def __init__(self, socket, addr):
        self.addr = addr
        self.socket = socket

    def send(self, up, down, left, right):
        data = {'event': {'up': up, 'down': down, 'left': left, 'right': right}}
        server_socket.message.send(self.socket, data)

    def receive(self):
        return server_socket.message.receive(self.socket)
