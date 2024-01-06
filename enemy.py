import pygame
from sprites import *
from load_images import load_image
from math import cos, sin, atan, radians, degrees
from Bullet import Bullet


class Enemy(pygame.sprite.Sprite):
    def __init__(self, health, damage, speed, anim, count_anim, types, ratefire, x, y, boss=False):
        super().__init__(enemy_sprites, all_sprites)
        self.rotation_angle = 0  # угол поворота противника
        self.boss = 1 + int(bool(boss))  # множитель сложности
        self.firetime = pygame.time.get_ticks()  # время прошлой атаки
        self.health = health
        self.damage = damage
        self.speed = speed
        self.ANIM_RIGHT = [load_image(anim.format(i), 2) for i in range(count_anim)]
        self.ANIM_LEFT = [pygame.transform.flip(self.ANIM_RIGHT[i].copy(), True, False) for i in range(count_anim)]
        self.count_anim = self.max_count_anim = count_anim  # кол-во кадров в анимации
        self.types = types  # тип противника
        self.ratefire = ratefire  # скорострельность
        self.image = self.ANIM_LEFT[0]
        self.w, self.h = [i // 2 for i in self.image.get_size()]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def change_image(self, image):
        """изменяет текущую картинку и маску противника"""
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)

    def go(self, angle):
        """сдвигает проивника согласно его скорости"""
        self.rect = self.rect.move(self.speed * cos(angle), -self.speed * sin(angle))
        return self.speed * cos(angle), -self.speed * sin(angle)

    def position(self, x1, y1):
        """Изменяет угол направления движения противника"""
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
        """аттакует персонажа"""
        if self.types in ('nearest', 'stay'):
            Bullet(self.rect.x + self.w * cos(self.rotation_angle), self.rect.y - self.h * sin(self.rotation_angle),
                   self.rotation_angle, 0, self.boss, self.damage, 'enemy', timelife=100)
        if self.types in ('faraway', 'stay'):
            Bullet(self.rect.x + self.w, self.rect.y + self.h, self.rotation_angle, 10 * self.boss,
                   self.boss, self.damage, 'enemy')

    def update(self, character, *args):
        if self.health <= 0:  # проверяет, жив противник или нет
            self.kill()
            return
        self.position(character.rect.x, character.rect.y)
        self.count_anim = (self.count_anim + 1) % self.max_count_anim
        if -90 <= degrees(self.rotation_angle) <= 90:
            self.change_image(self.ANIM_RIGHT[self.count_anim])
        else:
            self.change_image(self.ANIM_LEFT[self.count_anim])
        going = (0, 0)
        if self.types == 'nearest':
            going = self.go(self.rotation_angle)
        if self.types == 'faraway':
            # проверяем, нужно ли двигаться к персонажу
            if (self.rect.x - character.rect.x) ** 2 + (self.rect.y - character.rect.y) ** 2 > 10000:
                going = self.go(self.rotation_angle)
            elif -60 <= (self.rect.x - character.rect.x) ** 2 + (self.rect.y - character.rect.y) ** 2 - 10000 <= 60:
                going = (0, 0)
            else:
                going = self.go(-self.rotation_angle)
        if pygame.sprite.spritecollideany(self, location_sprites):  # столкновение со стеной
            self.go(*[-i for i in going])
        time = pygame.time.get_ticks()  # текущее время
        if self.firetime + self.ratefire < time:
            self.firetime = time
            self.attack()
