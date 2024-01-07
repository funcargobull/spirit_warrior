import pygame
import random
from database import Database
from characters import *
from sprites import *
from weapons import *
from enemyes import *

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


class UiElement(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, file, size, *groups):
        super().__init__(*groups)
        self.image = pygame.transform.scale(load_image(file), size)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y


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


class Text(pygame.sprite.Sprite):
    def __init__(self, text, size, color):
        super().__init__(ui_sprites)
        self.text = text
        self.size = size
        self.color = color
        self.font = pygame.font.Font("pixeleum.ttf", self.size)
        self.textSurf = self.font.render(self.text, True, self.color)
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image = pygame.Surface((W, H), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.image.blit(self.textSurf, (self.rect.x, self.rect.y))


class NewGame:
    def __init__(self, hero, wave):
        self.hero = hero
        self.wave = wave
        self.health_count = None
        self.energy_count = None
        self.armor_count = None
        self.money_count = None
        self.wave_count = None
        self.status = "wave_off"

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

        UiElement(15, 15, "pictures/ui/stats.png", (255, 122), ui_sprites)
        UiElement(1125, 15, "pictures/ui/coin_place.png", (100, 75), ui_sprites)
        UiElement(1150, 15, "pictures/ui/coin.png", (60, 67), ui_sprites)

        self.health_count = Text(f"{self.hero.health}/{self.hero.max_health}", 20, (255, 255, 255))
        self.armor_count = Text(f"{self.hero.armor}/{self.hero.max_armor}", 20, (255, 255, 255))
        self.energy_count = Text(f"{self.hero.energy}/{self.hero.max_energy}", 20, (255, 255, 255))
        self.money_count = Text(f"{self.hero.money}", 24, (255, 255, 255))
        self.wave_count = Text(f"Волна: {self.wave}", 24, (255, 255, 255))

    def update(self):
        ui_sprites.remove([self.health_count, self.armor_count, self.energy_count, self.money_count, self.wave_count])
        self.health_count = Text(f"{self.hero.health}/{self.hero.max_health}", 20, (255, 255, 255))
        self.health_count.rect.x = 130
        self.health_count.rect.y = 26

        self.armor_count = Text(f"{self.hero.armor}/{self.hero.max_armor}", 20, (255, 255, 255))
        self.armor_count.rect.x = self.health_count.rect.x
        self.armor_count.rect.y = self.health_count.rect.y + self.armor_count.rect.height + 3

        self.energy_count = Text(f"{self.hero.energy}/{self.hero.max_energy}", 20, (255, 255, 255))
        self.energy_count.rect.x = 105
        self.energy_count.rect.y = self.armor_count.rect.y + self.energy_count.rect.height + 4

        self.money_count = Text(f"{self.hero.money}", 30, (0, 0, 0))
        self.money_count.rect.x = 1225
        self.money_count.rect.y = 25

        self.wave_count = Text(f"Волна: {self.wave}", 30, (255, 255, 255))
        self.wave_count.rect.x = 1125
        self.wave_count.rect.y = 600

        if not enemy_sprites.sprites():
            # self.status = "wave_off"
            if self.wave < 2:
                self.wave += 1
            # seconds = (pygame.time.get_ticks() - start_ticks) / 1000
            # if seconds > 5:
                self.start_wave()

    def start_wave(self):
        self.status = "wave_on"
        for item in database.get_waves():
            if self.wave == item[0]:
                enemies = item[1]
        for enemy in enemies.split(";"):
            eval(f"{enemy}(random.randint(100, 1280), random.randint(100, 680))")
