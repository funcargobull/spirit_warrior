import pygame
from load_images import load_image
from math import degrees, sin, cos


class Weapon(pygame.sprite.Sprite):
    def __init__(self, damage, size_bullet, type_bullet, ratefire, image, cost_energy, cost, weapon_sprites,
                 all_sprites):
        super().__init__(weapon_sprites, all_sprites)
        self.damage = damage
        self.type_bullet = type_bullet
        self.ratefire = ratefire
        self.cost_energy = cost_energy
        self.cost = cost
        self.image = load_image(image, 2)
        self.orig_image = self.image.copy()
        self.rect = self.image.get_rect()
        self.w, self.h = self.image.get_size()
        self.size_bullet = size_bullet
        self.time_shot = pygame.time.get_ticks()

    def attack(self):
        time = pygame.time.get_ticks()
        if self.time_shot + self.ratefire <= time:
            self.type_bullet(self.rect.x, self.rect.y, self.size_bullet)
            self.time_shot = time

    def update(self, character):
        angle = character.rotation_angle
        xc, yc = character.xc, character.yc
        image = self.orig_image
        if not character.location:
            image = pygame.transform.flip(self.orig_image, False, True)
            xc = character.w - character.xc
        self.image = pygame.transform.rotate(image, degrees(angle))
        self.rect.x = character.rect.x + xc
        self.rect.y = character.rect.y + yc
        self.rect = self.image.get_rect(center=(self.rect.x, self.rect.y))  # передвигаем оружие в центр персонажа
        self.rect.x += self.w * cos(angle) // 2
        self.rect.y -= self.h * sin(angle) // 2
