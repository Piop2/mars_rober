import pygame

from server_socket.error import ClientNotConnected, NoDataReceived


class Renderer:
    def __init__(self, app):
        self.app = app

        # fps
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.dt = 0

        # controller
        self.axis_r = 13

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

        # render controller
        assets = self.app.assets
        k = self.app.input

        controller = pygame.Surface(assets.c_body.get_size())
        controller.fill((100, 0, 0))
        controller.set_colorkey((100, 0, 0))

        controller.blit(assets.c_body, (0, 0))  # body

        # axis1
        axis1 = k.axis1
        # hint arrow
        assets.a_up.set_alpha(55)
        assets.a_down.set_alpha(55)
        if axis1[1] < 0:
            assets.a_up.set_alpha(55 + (200 * abs(axis1[1])))
        else:
            assets.a_down.set_alpha(55 + (200 * abs(axis1[1])))
        controller.blit(assets.a_up, (60, 25))
        controller.blit(assets.a_down, (60, 120))
        # stick
        controller.blit(assets.c_ball, (50, 50))
        controller.blit(assets.c_stick, (65 + (axis1[0] * self.axis_r), 55 + (axis1[1] * self.axis_r)))

        # axis2
        axis2 = k.axis2
        # hint arrow
        assets.a_left.set_alpha(55)
        assets.a_right.set_alpha(55)
        if axis2[0] < 0:
            assets.a_left.set_alpha(55 + (200 * abs(axis2[0])))
        else:
            assets.a_right.set_alpha(55 + (200 * abs(axis2[0])))
        controller.blit(assets.a_left, (215, 130))
        controller.blit(assets.a_right, (310, 130))
        # stick
        controller.blit(assets.c_ball, (240, 120))
        controller.blit(assets.c_stick, (255 + (axis2[0] * self.axis_r), 125 + (axis2[1] * self.axis_r)))

        display.blit(controller, (((display.get_width() / 2) - (controller.get_width() / 2)), 400))

        self.app.window.render()

        pygame.display.update()
