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

        # # client camera img
        # image = None
        # try:
        #     # if client worked, receive the data(pygame.Surface)
        #     image = self.app.server.client_camera_img
        # except ClientNotConnected:  # if client not connected
        #     pass
        # except NoDataReceived:  # if client didnt received data or img data
        #     pass
        #
        # # finally render image to window
        # display.blit(image, (0, 0))

        # render button
        assets = self.app.assets
        k = self.app.input
        for buttons, pos, pressed in zip((assets.b_up, assets.b_down, assets.b_left, assets.b_right),
                                         ((225, 120), (225, 220), (175, 170), (275, 170)),
                                         (k.up, k.down, k.left, k.right)):
            if pressed:
                button = buttons[1]
            else:
                button = buttons[0]

            display.blit(button, pos)

        self.app.window.render()

        pygame.display.update()
