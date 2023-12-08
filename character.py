import pygame
from math import atan

WEIGHT = 0  # ширина персонажа
HEIGHT = 0  # высота персонажа


class Character(pygame.sprite.Sprite):
    def __int__(self, health, armor, energy, weapons, x, y, anim, speed, *args):
        super().__init__(*args)
        self.location = True  # если True, персонаж смотрит вправо, иначе влево
        self.rotation_angle = 0  # угол поворота оружия относительно персонажа
        # путь к анимации передается в формате название_файла{}.формат, где на месте {} будут стоять номера спрайтов
        self.ANIM_RIGHT = [pygame.image.load(anim.format(i)) for i in range(8, 16)]
        self.ANIM_STAY = [pygame.image.load(anim.format(i)) for i in range(0, 8)]
        self.ANIM_LEFT = [pygame.transform.flip(self.ANIM_RIGHT[i], True, False) for i in range(8)]
        self.animcount = 0
        self.image = self.ANIM_STAY[self.animcount]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # характеистики персонажа
        self.speed = speed
        self.health = self.max_health = health
        self.armor = self.max_armor = armor
        self.energy = self.max_energy = energy
        self.weapons = weapons

    def go(self, x, y):
        """сдвигает персонажа согласно его скорости.
        Для свдига по осям x, y необходимо передать 1 или -1 там где необходимо сдвинуть, иначе 0"""
        pass

    def position(self, x1, y1):
        """на вход подаются координаты ближайшего противника. Изменяет угол направления оружия"""
        delta_x, delta_y = x1 - self.rect.x, y1 - self.rect.y
        self.rotation_angle = atan(delta_y / delta_x)

    def attack(self):
        self.weapons[0].attack()

    def change_weapon(self):
        """меняет оружие в руках персонажа"""
        weapon = self.weapons.pop(0)
        self.weapons.append(weapon)

    def update(self, events, enemies):
        if len(enemies) != 0:
            min_distance_enemy = min(enemies, key=lambda enemy: ((self.rect.x - enemy.rect.x) ** 2 + (
                    self.rect.y - enemy.rect.y) ** 2) ** 0.5)
            self.position(min_distance_enemy.rect.x, min_distance_enemy.rect.y)
        else:
            self.rotation_angle = 0
        pass
