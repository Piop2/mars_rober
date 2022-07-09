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
    
    def fullscreen(self):
        return
    
    def windowscreen(self):
        return
    
