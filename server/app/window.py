import pygame


class Window:
    def __init__(self):
        # monitor size
        self.monitor_size = None # plz get monitor size
        
        # window: real program window
        self.window_size = (500, 500)
        self.window = pygame.display.set_mode(self.window_size)
        # render surface
        self.display_size = (500, 500)
        self.display = pygame.Surface(self.display_size)

        # caption
        pygame.display.set_caption('Rober Controll')

        self.is_fullscreen = False
    
    def render(self):
        if self.is_fullscreen:
            size = self.monitor_size
        else:
            size = self.window_size
        self.window.blit(pygame.transform.scale(self.display, size), (0, 0))

    def fullscreen(self):
        return
    
    def windowscreen(self):
        return
    
