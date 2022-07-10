import pygame.image

from utils.clip import clip
from utils.json_data import load_f


def load_button(path):
    img = pygame.image.load(path)
    button_img = (
        clip(img, 0, 0, 50, 50),
        clip(img, 55, 0, 50, 50)
    )
    return button_img


class Assets:
    def __init__(self):
        self.b_up = load_button('assets/buttons/up.png')
        self.b_down = load_button('assets/buttons/down.png')
        self.b_left = load_button('assets/buttons/left.png')
        self.b_right = load_button('assets/buttons/right.png')
