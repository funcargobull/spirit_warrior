import pygame
import random
from characters import *
from sprites import *
from weapons import *
from enemyes import *
from database import Database
from load_images import load_image

database = Database()

# элемент пользовательского интерфейса
class UiElement(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, file, size, *groups):
        super().__init__(*groups)
        self.image = pygame.transform.scale(load_image(file), size)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

# пол
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, *groups):
        super().__init__(*groups)
        self.image = load_image("pictures/map/stone.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

# стена
class Wall(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, *groups):
        super().__init__(*groups)
        self.image = load_image("pictures/map/cobblestone.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

# текст
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

# показ текущего оружия
class WeaponShow(pygame.sprite.Sprite):
    def __init__(self, character, pos_x, pos_y, *groups):
        super().__init__(*groups)
        self.image = load_image(character.weapons[0].image_, 2)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

# торговец
class Seller(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, *groups):
        super().__init__(*groups)
        self.image = load_image("pictures/ui/seller.png", 2)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

# класс новой игры
class NewGame:
    def __init__(self, hero, wave):
        self.hero = hero
        self.wave = wave
        self.health_count = None
        self.energy_count = None
        self.armor_count = None
        self.money_count = None
        self.wave_count = None
        self.weapon_show = None
        self.weapon_cost_energy_show = None
        self.show_e = None

    # создание пользовательского интерфейса (пол, стены, статистика, торговец, счетчик волны и оружие)
    def setup(self, w=1380, h=780):
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
        UiElement(1125, 15, "pictures/ui/coin_place.png",
                  (168, 75), ui_sprites)
        UiElement(1150, 18, "pictures/ui/coin.png", (60, 67), ui_sprites)
        Seller(80, 640, ui_sprites, seller)

        self.weapon_show = WeaponShow(self.hero, 1150, 670, ui_sprites)
        self.weapon_cost_energy_show = Text(
            f"{self.hero.weapons[0].cost_energy}", 24, (139, 139, 250))

        self.health_count = Text(
            f"{self.hero.health}/{self.hero.max_health}", 20, (255, 255, 255))
        self.armor_count = Text(
            f"{self.hero.armor}/{self.hero.max_armor}", 20, (255, 255, 255))
        self.energy_count = Text(
            f"{self.hero.energy}/{self.hero.max_energy}", 20, (255, 255, 255))
        self.money_count = Text(f"{self.hero.money}", 24, (255, 255, 255))
        self.wave_count = Text(f"Волна: {self.wave}", 24, (255, 255, 255))

        # показ буквы Е при приближении к торговцу
        self.show_e = Text("E", 20, (255, 255, 255))
        self.show_e.rect.x = self.hero.rect.x + self.show_e.rect.width // 2
        self.show_e.rect.y = self.hero.rect.y - 10

    # постоянное обновление спрайтов
    def update(self):
        ui_sprites.remove([self.health_count, self.armor_count, self.energy_count,
                          self.money_count, self.wave_count, self.weapon_show, self.weapon_cost_energy_show, self.show_e])

        self.health_count = Text(
            f"{self.hero.health}/{self.hero.max_health}", 20, (255, 255, 255))
        self.health_count.rect.x = 130
        self.health_count.rect.y = 26

        self.armor_count = Text(
            f"{self.hero.armor}/{self.hero.max_armor}", 20, (255, 255, 255))
        self.armor_count.rect.x = self.health_count.rect.x
        self.armor_count.rect.y = self.health_count.rect.y + \
            self.armor_count.rect.height + 3

        self.energy_count = Text(
            f"{self.hero.energy}/{self.hero.max_energy}", 20, (255, 255, 255))
        self.energy_count.rect.x = 105
        self.energy_count.rect.y = self.armor_count.rect.y + \
            self.energy_count.rect.height + 4

        self.money_count = Text(f"{self.hero.money}", 30, (255, 255, 255))
        self.money_count.rect.x = 1225
        self.money_count.rect.y = 28

        self.wave_count = Text(f"Волна: {self.wave}", 30, (255, 255, 255))
        self.wave_count.rect.x = 1125
        self.wave_count.rect.y = 600

        self.weapon_show = WeaponShow(self.hero, 1150, 670, ui_sprites)
        self.weapon_show.rect.x = 1150
        self.weapon_show.rect.y = 670

        self.weapon_cost_energy_show = Text(
            f"{self.hero.weapons[0].cost_energy}", 24, (255, 255, 255))
        self.weapon_cost_energy_show.rect.x = self.weapon_show.rect.x + \
            self.weapon_show.rect.width + self.weapon_cost_energy_show.rect.width + 5
        self.weapon_cost_energy_show.rect.y = self.weapon_show.rect.y - 8

        # появление буквы Е
        if pygame.sprite.spritecollideany(self.hero, seller):
            self.show_e = Text("E", 20, (255, 255, 255))
            self.show_e.rect.x = self.hero.rect.x
            self.show_e.rect.y = self.hero.rect.y - 25

        if not enemy_sprites.sprites():
            self.wave += 1
            self.hero.wave += 1

            tmp_weapons = [weapon.__class__.__name__ for weapon in self.hero.weapons]
            database.update_data(str(self.hero.__class__.__name__), self.hero.wave, ";".join(tmp_weapons), self.hero.money)
            if self.wave <= 15:
                self.start_wave()

    # начало новой волны
    def start_wave(self):
        # получение врагов из БД и прорисовка
        for item in database.get_waves():
            if self.wave == item[0]:
                enemies = item[1]
        for enemy in enemies.split(";"):
            obj = eval(f"{enemy}(0, 0)")
            obj.rect.x = random.randint(120 + obj.rect.width + 20, 1220 - obj.rect.width - 20)
            obj.rect.y = random.randint(60 + obj.rect.height + 20, 560 - obj.rect.height - 20)
