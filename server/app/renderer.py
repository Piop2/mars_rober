import pygame

from server_socket.error import ClientNotConnected, NoDataReceived

class Renderer:
    def __init__(self, app):
        self.app = app

        # fps
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.dt = 0

    def update(self):
        # display
        display = self.app.window.display

        self.dt = self.clock.tick(self.fps)

        display.fill((255, 255, 255))

        # client camera img
        image = None
        try:
            # if client worked, receive the data(pygame.Surface)
            image = self.app.server.client_camera_img
        except ClientNotConnected: # if client not connected
            pass
        except NoDataReceived: # if client didnt received data or img data
            pass

        # finally render image to window
        display.blit(image, (0, 0))

        pygame.display.update()
