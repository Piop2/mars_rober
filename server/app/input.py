import sys
import pygame


class Input:
    def __init__(self, app):
        pygame.joystick.init()

        self.app = app

        # controller: EX Band
        self.controller = None
        # controller axis pos
        self.axis1 = [0, 0]
        self.axis2 = [0, 0]
        # # hat
        # self.h_up = False
        # self.h_down = False
        # self.h_left = False
        # self.h_right = False

        # keys
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def get_controller(self):
        try:
            # get first controller
            self.controller = pygame.joystick.Joystick(0)
        except RuntimeError:
            self.controller = None
        return

    def update(self):
        self.get_controller()

        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # controller
            if self.controller is not None:
                self.axis1 = [self.controller.get_axis(0), self.controller.get_axis(1)]
                self.axis2 = [self.controller.get_axis(3), self.controller.get_axis(4)]

            if event.type == pygame.JOYHATMOTION:
                if event.value == (0, 1):  # hat up
                    self.up = True
                if event.value == (0, -1):  # hat down
                    self.down = True
                if event.value == (1, 0):  # hat right
                    self.right = True
                if event.value == (-1, 0):  # hat left
                    self.left = True
                if event.value == (0, 0):  # hat center
                    self.up = False
                    self.down = False
                    self.right = False
                    self.left = False
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:
                    if event.value > 0:
                        self.right = True
                    elif event.value < 0:
                        self.left = True
                    else:
                        self.left = False
                        self.right = False
                if event.axis == 4 or event.axis == 5:
                    if event.value > 0:
                        self.down = True
                    elif event.value < 0:
                        self.up = True
                    else:
                        self.up = False
                        self.down = False
            # if event.type == pygame.JOYHATMOTION:
            #     if event.value[0] == 1:
            #         self.h_up = True
            #     else:
            #         self.h_up = False
            #     if event.value[0] == -1:
            #         self.h_down = True
            #     else:
            #         self.h_down = False
            #     if event.value[1] == 1:
            #         self.h_right = True
            #     else:
            #         self.h_right = False
            #     if event.value[1] == -1:
            #         self.h_left = True
            #     else:
            #         self.h_left = False

            # keyboard
            if event.type == pygame.KEYDOWN:
                # up
                if event.key == pygame.K_w:
                    self.up = True
                # down
                if event.key == pygame.K_s:
                    self.down = True
                # left
                if event.key == pygame.K_a:
                    self.left = True
                # right
                if event.key == pygame.K_d:
                    self.right = True
                
                # togle fullscreen&windowscreen
                if event.key == pygame.K_f:
                    self.app.window.is_fullscreen = not self.app.window.is_fullscreen
                    if self.app.window.is_fullscreen:
                        self.app.window.fullscreen()
                    else:
                        self.app.window.windowscreen()

            if event.type == pygame.KEYUP:
                # up
                if event.key == pygame.K_w:
                    self.up = False
                # down
                if event.key == pygame.K_s:
                    self.down = False
                # left
                if event.key == pygame.K_a:
                    self.left = False
                # right
                if event.key == pygame.K_d:
                    self.right = False
        return
