import pygame
from database import Database
from characters import *
from sprites import *
from weapons import *

database = Database()


# Загрузка картинки
def load_image(fullname, colorkey=None):
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, *groups):
        super().__init__(*groups)
        self.image = load_image("pictures/map/stone.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y


class Wall(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, *groups):
        super().__init__(*groups)
        self.image = load_image("pictures/map/cobblestone.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y


class NewGame:
    def __init__(self, hero, wave):
        self.hero = hero
        self.wave = wave

    def setup(self, w, h):
        for x in range(0, w, 60):
            Wall(x, 0, walls, camera_entities)
            Wall(x, h - 60, walls, camera_entities)
        for y in range(60, h, 60):
            Wall(0, y, walls, camera_entities)
            Wall(w - 60, y, walls, camera_entities)
        for y in range(60, h - 60, 60):
            for x in range(60, w - 60, 60):
                Tile(x, y, tiles, camera_entities)

