import pygame
from database import Database

database = Database()


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


class Camera:
    # Зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # Сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # Позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


class NewGame:
    def __init__(self, group, hero_name, wave):
        self.group = group
        self.hero_name = hero_name
        self.wave = wave

    def setup(self, walls, tiles):
        Wall(0, 0, walls)
        # for x in range(0, 1920, 60):
        #     Wall(x, 60, walls)
        # Wall(0, 600, walls)
