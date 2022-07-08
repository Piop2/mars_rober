import pygame.image

from utils.clip import clip


def load_button(path):
    img = pygame.image.load(path)
    button_img = (
        clip(img, 0, 0, 50, 50),
        clip(img, 55, 0, 50, 50)
    )
    return button_img


class Assets:
    def __init__(self):
        self.b_up = load_button('images/button_up.png')
        self.b_down = load_button('images/button_down.png')
        self.b_left = load_button('images/button_left.png')
        self.b_right = load_button('images/button_right.png')
