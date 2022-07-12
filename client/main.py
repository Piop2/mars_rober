"""
ROVER APP
"""
from client_socket.client import ClientSocket


class Rover:
    def __init__(self):
        self.client = ClientSocket(self)

    def update(self):
        return

    def run(self):
        self.client.run()
        while True:
            self.update()


if __name__ == '__main__':
    Rover().run()
