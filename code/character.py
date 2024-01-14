import pygame
from math import atan, degrees, radians
from load_images import load_image
from sprites import *


class Character(pygame.sprite.Sprite):
    def __init__(self, health, armor, energy, weapons, x, y, anim, speed, xc, yc):
        super().__init__(character_sprites)
        self.location = True  # если персонаж смотрит вправо, то True, иначе False
        self.rotation_angle = 0  # угол поворота оружия относительно персонажа
        # время, используемое для восстановления брони
        self.armor_tick = pygame.time.get_ticks()
        # время, используемое для восстановления способности
        self.ulta_tick = pygame.time.get_ticks()
        # время, используемое для смены оружия
        self.change_weapon_tick = pygame.time.get_ticks()
        # путь к анимации передается в формате название_файла{}.формат, где на месте {} будут стоять номера спрайтов
        self.ANIM_DEATH = load_image(anim.format(16), 2)
        self.ANIM_RIGHT = [load_image(anim.format(i), 2) for i in range(8, 16)]
        self.ANIM_STAY_RIGHT = [load_image(
            anim.format(i), 2) for i in range(0, 8)]
        self.ANIM_STAY_LEFT = [pygame.transform.flip(
            self.ANIM_STAY_RIGHT[i].copy(), True, False) for i in range(8)]
        self.ANIM_LEFT = [pygame.transform.flip(
            self.ANIM_RIGHT[i].copy(), True, False) for i in range(8)]
        self.animcount = 0
        self.image = self.ANIM_STAY_RIGHT[self.animcount]
        self.w, self.h = self.image.get_size()
        self.xc, self.yc = xc * 2, yc * 2  # центр изображения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # характеистики персонажа
        self.speed = speed
        self.health = self.max_health = health
        self.armor = self.max_armor = armor
        self.energy = self.max_energy = energy
        self.weapons = weapons
        self.money = 70
        self.on_sell = False
        # стены
        self.walls = walls
        # волна
        self.wave = 1
        # играем или нет
        self.gaming = False

    def update_armor(self):
        """восстанавливает броню персонажа"""
        time = pygame.time.get_ticks()
        if self.armor_tick + 5000 <= time:  # время восстановления
            self.armor += 1
            if self.armor < self.max_armor:
                # убираем время, чтобы броня восстанавливалась по 1 еденице в секунду
                self.armor_tick += 500

    def go(self, x, y):
        """сдвигает персонажа согласно его скорости.
        Для свдига по осям x, y необходимо передать 1 или -1 там где необходимо сдвинуть, иначе 0"""
        self.rect = self.rect.move(self.speed * x, self.speed * y)
        return x, y

    def position(self, x1, y1):
        """Изменяет угол направления оружия"""
        delta_x, delta_y = x1 - self.rect.x, y1 - self.rect.y
        if delta_x != 0:
            self.rotation_angle = abs(atan(delta_y / delta_x))
            if x1 < self.rect.x:
                self.rotation_angle = radians(180) - self.rotation_angle
            if y1 > self.rect.y:
                self.rotation_angle = -self.rotation_angle
        else:
            self.rotation_angle = 0

    def attack(self):
        """аттакует, используя выбранное оружие"""
        self.weapons[0].attack(self)

    def change_weapon(self):
        """меняет оружие в руках персонажа"""
        time_action, time = 200, pygame.time.get_ticks()
        if self.change_weapon_tick + time_action < time:
            weapon = self.weapons.pop(0)
            self.weapons.append(weapon)
            self.change_weapon_tick = time

    def change_image(self, image):
        """изменяет текущую картинку и маску персонажа"""
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)

    def ulta(self):
        """уникальная способность персонажа"""
        pass

    def update(self, events, pos):
        if self.health <= 0:  # проевряем, жив ли персонаж
            self.kill()
            return

        self.position(*pos)
        going = []
        if self.armor == self.max_armor:
            self.armor_tick = pygame.time.get_ticks()
        else:
            self.update_armor()
        self.animcount = (self.animcount + 1) % 8
        keys = pygame.key.get_pressed()  # список всех нажатых клавиш клавиатуры
        # определяем направление движения персонажа
        if keys[pygame.K_a] or keys[pygame.K_s]:
            self.change_image(self.ANIM_LEFT[self.animcount])
            self.location = False
        elif keys[pygame.K_d] or keys[pygame.K_w]:
            self.change_image(self.ANIM_RIGHT[self.animcount])
            self.location = True
        elif -90 <= degrees(self.rotation_angle) <= 90:
            self.change_image(self.ANIM_STAY_RIGHT[self.animcount])
            self.location = True
        else:
            self.change_image(self.ANIM_STAY_LEFT[self.animcount])
            self.location = False
        mouse_click = pygame.mouse.get_pressed()  # список всех нажатых клавиш мыши
        if mouse_click[0]:
            self.attack()
        if mouse_click[2]:
            self.ulta()
        if keys[pygame.K_q]:
            self.change_weapon()
        if keys[pygame.K_w]:
            going.append(self.go(0, -1))
        if keys[pygame.K_a]:
            going.append(self.go(-1, 0))
        if keys[pygame.K_s]:
            going.append(self.go(0, 1))
        if keys[pygame.K_d]:
            going.append(self.go(1, 0))
        # столкновение со стеной
        if pygame.sprite.spritecollideany(self, walls):
            for g in going:
                self.go(*[-i for i in g])
        self.weapons[0].update(self)
