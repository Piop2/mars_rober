import pygame
import math


class Window:
    def __init__(self):
        pygame.init()

        # monitor size
        self.monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]

        # window: real program window
        self.window_size = (1000, 750)
        self.window = pygame.display.set_mode(self.window_size)
        # render surface
        self.display_size = (800, 600)
        self.display = pygame.Surface(self.display_size)

        # caption
        pygame.display.set_caption('Rober Controll')

        self.is_fullscreen = False

    def render(self):
        if self.is_fullscreen:
            size = (1440, 1080)
            pos = ((self.monitor_size[0] / 2) - (size[0] / 2), (self.monitor_size[1] / 2) - (size[1] / 2))

        else:  # if windowscreen mode
            size = self.window_size
            pos = (0, 0)

        self.window.blit(pygame.transform.scale(self.display, size), pos)
        return

    def fullscreen(self):
        pygame.display.set_mode(self.monitor_size, pygame.FULLSCREEN)
        return

    def windowscreen(self):
        pygame.display.set_mode(self.window_size)
