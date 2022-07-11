import pygame.image

from utils.clip import clip


def load_button(path):
    img = pygame.image.load(path)
    button_img = (
        clip(img, 0, 0, 50, 50),
        clip(img, 55, 0, 50, 50)
    )
    return button_img


def load_img(path):
    return pygame.image.load(path)


class Assets:
    def __init__(self):
        self.c_body = load_img('assets/controller/body.png')

        # axis
        self.c_ball = load_img('assets/controller/axis/ball.png')
        self.c_stick = load_img('assets/controller/axis/stick.png')

        # arrow
        self.a_up = load_img('assets/arrow/up.png')
        self.a_down = load_img('assets/arrow/down.png')
        self.a_left = load_img('assets/arrow/left.png')
        self.a_right = load_img('assets/arrow/right.png')

        # hat
        self.h_c = load_img('assets/controller/hat/00.png')
        self.h_up = load_img('assets/controller/hat/01.png')
        self.h_down = load_img('assets/controller/hat/0-1.png')
        self.h_right = load_img('assets/controller/hat/10.png')
        self.h_left = load_img('assets/controller/hat/-10.png')
