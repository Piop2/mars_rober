import sys
import pygame


class Input:
    def __init__(self, app):
        self.app = app

        # keys
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def update(self):
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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
