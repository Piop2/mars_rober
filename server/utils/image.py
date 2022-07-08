import pygame


def encode_image(surface):
    surf_bytes = pygame.image.tostring(surface, 'RGB')
    surf_size = surface.get_size()
    return {'bytes': surf_bytes, 'size': surf_size}


def decode_image(img_data):
    surf_bytes = img_data['bytes']
    surf_size = img_data['size']
    surf = pygame.image.fromstring(surf_bytes, surf_size, 'RGB')
    return surf.copy()
