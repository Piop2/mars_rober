import pygame


class Renderer:
    def __init__(self, app):
        self.app = app

        # fps
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.dt = 0

    def update(self):
        self.dt = self.clock.tick(self.fps)

        self.app.window.display.fill((255, 255, 255))

        pygame.display.update()
