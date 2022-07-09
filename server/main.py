from app.window import Window
from app.renderer import Renderer
from app.input import Input
from app.assets import Assets

from server_socket.server import ServerSocket


class Main:
    def __init__(self):
        self.assets = Assets()
        self.window = Window()
        self.renderer = Renderer(self)
        self.input = Input()
        self.server = ServerSocket(self)

    def update(self):
        self.renderer.update()
        self.input.update()

    def run(self):
        self.server.run()

        while True:
            self.update()


if __name__ == '__main__':
    Main().run()
