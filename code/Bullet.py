from sprites import *
from load_images import load_image
from math import cos, sin, degrees
import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, speed, size, damage, relation, timelife=None):
        super().__init__(bullet_sprites, all_sprites, camera_entities)
        if timelife is not None:
            self.image = pygame.transform.rotate(load_image('pictures/weapons/bullet_knife.png', size), degrees(angle))
        elif relation == 'friend':
            self.image = load_image('pictures/weapons/bullet_39.png', size)
        else:
            self.image = load_image('pictures/weapons/bullet_37.png', size)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.angle = angle  # угол поворота
        self.speed = speed
        self.damage = damage
        self.relation = relation  # принадлежность пули (своя или противника)
        self.time = pygame.time.get_ticks()  # время появления
        self.timelife = timelife  # время жизни пули (если необходимо)

    def update(self, *args):
        # проверяем должна ли быть жива пуля
        if self.timelife is not None and self.time + self.timelife < pygame.time.get_ticks():
            self.kill()
            return
        self.rect.x += self.speed * cos(self.angle)
        self.rect.y += -self.speed * sin(self.angle)
        if pygame.sprite.spritecollideany(self, walls):  # столкновение со стеной
            self.kill()
        for b in pygame.sprite.spritecollide(self, bullet_sprites, False):  # столкновение с другой пулей
            if b.relation != self.relation:
                b.kill()
                self.kill()
        if self.relation == 'friend':  # если пуля своя, наносим уррон врагу
            enemy = pygame.sprite.spritecollide(self, enemy_sprites, False)
            if len(enemy) > 0:
                enemy[0].health -= self.damage
                self.kill()
        else:
            # если пуля противника, сначала уничтожаем броню персонажа, а затем его здоровье
            character = pygame.sprite.spritecollide(self, character_sprites, False)
            if len(character) > 0:
                character[0].armor_tick = pygame.time.get_ticks()
                if character[0].armor > 0:
                    character[0].armor = max(character[0].armor - self.damage, 0)
                else:
                    character[0].health -= self.damage
                self.kill()