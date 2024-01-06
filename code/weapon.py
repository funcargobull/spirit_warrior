from load_images import load_image
from math import degrees, sin, cos
from sprites import *
from Bullet import Bullet


class Weapon(pygame.sprite.Sprite):
    def __init__(self, damage, size_bullet, type_bullet, ratefire, image, cost_energy, cost, speed_bullet):
        super().__init__(weapons_sprites, all_sprites)
        self.damage = damage
        self.type_bullet = type_bullet
        self.speed_bullet = speed_bullet
        self.ratefire = ratefire
        self.cost_energy = cost_energy
        self.cost = cost
        self.image = load_image(image, 2)
        self.mask = pygame.mask.from_surface(self.image)
        self.orig_image = self.image.copy()
        self.rect = self.image.get_rect()
        self.w, self.h = self.image.get_size()
        self.size_bullet = size_bullet
        self.time_shot = pygame.time.get_ticks()
        self.angle = 0

    def attack(self, character):
        """аттакует противника"""
        time = pygame.time.get_ticks()  # текущее время
        # проверяем, есть ли енергия для стрельбы и прошли ли для этого достаточно времени
        if self.time_shot + self.ratefire <= time and character.energy - self.cost_energy >= 0:
            character.energy -= self.cost_energy
            if self.type_bullet == 'sword':
                bullet = pygame.sprite.spritecollide(self, bullet_sprites, True)  # столкновение с пулей
                Bullet(self.rect.x + self.w * cos(self.angle) // 2, self.rect.y - self.h * sin(self.angle) // 2,
                       self.angle, 0, self.size_bullet, self.damage, 'friend', timelife=100)
            else:
                Bullet(self.rect.x, self.rect.y, self.angle, self.speed_bullet,
                       self.size_bullet, self.damage, 'friend')
            self.time_shot = time

    def update(self, character):
        self.angle = character.rotation_angle
        xc, yc = character.xc, character.yc
        image = self.orig_image
        if not character.location:
            image = pygame.transform.flip(self.orig_image, False, True)
            xc = character.w - character.xc  # отзеркаливаем позицию для оружия
        self.image = pygame.transform.rotate(image, degrees(self.angle))  # поворачиваем картинку
        self.rect.x = character.rect.x + xc
        self.rect.y = character.rect.y + yc
        self.rect = self.image.get_rect(center=(self.rect.x, self.rect.y))  # передвигаем оружие в центр персонажа
        self.rect.x += self.w * cos(self.angle) // 2
        self.rect.y -= self.h * sin(self.angle)

    def draw(self, screen):
        """рисует объект на плоскость"""
        screen.blit(self.image, self.rect)
