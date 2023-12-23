from os import path
from sys import exit
import pygame


def load_image(name, scale, colorkey=None):
    # если файл не существует, то выходим
    if not path.isfile(name):
        print(f"Файл с изображением '{name}' не найден")
        exit()
    image = pygame.image.load(name)
    width, height = image.get_size()
    image = pygame.transform.scale(image, (width * scale, height * scale))
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image
