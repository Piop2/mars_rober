import pygame


class Window:
    def __init__(self):
        pygame.init()

        # monitor size
        self.monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]  # plz get monitor size

        # window: real program window
        self.window_size = (750, 750)
        self.window = pygame.display.set_mode(self.window_size)
        # render surface
        self.display_size = (500, 500)
        self.display = pygame.Surface(self.display_size)

        # caption
        pygame.display.set_caption('Rober Controll')

        self.is_fullscreen = False

    def render(self):
        if self.is_fullscreen:  # if fullscreen mode
            w_ = self.monitor_size[0] / self.display_size[0]
            h_ = self.monitor_size[1] / self.display_size[0]
            if w_ >= h_:
                size = (int(self.display_size[0] * h_), int(self.display_size[1] * h_))
            else:
                size = (int(self.display_size[0] * w_), int(self.display_size[1] * w_))
            pos = ((self.monitor_size[0] / 2) - (size[0] / 2),
                   (self.monitor_size[1] / 2) - (size[1] / 2))
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
