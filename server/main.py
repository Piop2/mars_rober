from app.window import Window
from app.renderer import Renderer
from app.input import Input


class Main:
    def __init__(self):
        self.window = Window()
        self.renderer = Renderer(self)
        self.input = Input()

    def update(self):
        self.renderer.update()
        self.input.update()

    def run(self):
        while True:
            self.update()


if __name__ == '__main__':
    Main().run()
