import pygame
from sprites import *
from load_images import load_image
from math import cos, sin


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, speed, size, damage, relation):
        super().__init__(bullet_sprites, all_sprites)
        self.image = load_image('picturies/weapons/bullet_39.png', size) if relation == 'friend' else load_image(
            'picturies/weapons/bullet_37.png', size)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.angle = angle
        self.speed = speed
        self.damage = damage
        self.relation = relation

    def update(self, *args):
        self.rect.x += self.speed * cos(self.angle)
        self.rect.y += -self.speed * sin(self.angle)
        if pygame.sprite.spritecollideany(self, location_sprites):  # удар об стену
            self.kill()
        if self.relation == 'friend':
            enemy = pygame.sprite.spritecollide(self, enemy_sprites, False)
            if len(enemy) > 0:
                enemy[0].health -= self.damage
                self.kill()
        else:
            character = pygame.sprite.spritecollide(self, character_sprites, False)
            if len(character) > 0:
                character[0].health -= self.damage
                self.kill()
