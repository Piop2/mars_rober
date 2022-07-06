import pygame


class Window:
    def __init__(self):
        # window
        self.display_size = (500, 500)
        self.display = pygame.display.set_mode(self.display_size)

        # caption
        pygame.display.set_caption('Rober Controll')