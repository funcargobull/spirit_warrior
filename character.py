import pygame
from math import atan, degrees

WEIGHT = 0  # ширина персонажа
HEIGHT = 0  # высота персонажа


class Character(pygame.sprite.Sprite):
    def __init__(self, health, armor, energy, weapons, x, y, anim, speed, character_sprites, all_sprites):
        super().__init__(character_sprites, all_sprites)
        self.location = True  # если True, персонаж смотрит вправо, иначе влево
        self.rotation_angle = 0  # угол поворота оружия относительно персонажа
        # путь к анимации передается в формате название_файла{}.формат, где на месте {} будут стоять номера спрайтов
        self.ANIM_RIGHT = [pygame.image.load(anim.format(i)) for i in range(8, 16)]
        self.ANIM_STAY = [pygame.image.load(anim.format(i)) for i in range(0, 8)]
        self.ANIM_LEFT = [pygame.transform.flip(self.ANIM_RIGHT[i].copy(), True, False) for i in range(8)]
        self.animcount = 0
        self.image = self.ANIM_STAY[self.animcount]
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

    def go(self, x, y):
        """сдвигает персонажа согласно его скорости.
        Для свдига по осям x, y необходимо передать 1 или -1 там где необходимо сдвинуть, иначе 0"""
        self.rect = self.rect.move(self.speed * x, self.speed * y)
        pass

    def position(self, x1, y1):
        """Изменяет угол направления оружия"""
        delta_x, delta_y = x1 - self.rect.x, y1 - self.rect.y
        if delta_x != 0:
            self.rotation_angle = atan(delta_y / delta_x)
            if x1 < self.rect.x:
                self.rotation_angle = -abs(self.rotation_angle)
            else:
                self.rotation_angle = abs(self.rotation_angle)
        else:
            self.rotation_angle = 0

    def attack(self):
        """аттакует, используя выбранное оружие"""
        self.weapons[0].attack()

    def change_weapon(self):
        """меняет оружие в руках персонажа"""
        weapon = self.weapons.pop(0)
        self.weapons.append(weapon)

    def change_image(self, image):
        """изменяет текущую картинку и маску персонажа"""
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)

    def ulta(self):
        """уникальная способность персонажа"""
        pass

    def interaction(self):
        """взаимодействие с объектами, с которыми оно возможно"""
        pass

    def update(self, events, pos):
        self.position(*pos)
        self.animcount = (self.animcount + 1) % 8
        keys = pygame.key.get_pressed()
        if not keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.change_image(self.ANIM_STAY[self.animcount])
        elif 0 <= degrees(self.rotation_angle) <= 90:
            self.change_image(self.ANIM_RIGHT[self.animcount])
        else:
            self.change_image(self.ANIM_LEFT[self.animcount])
        for e in events:  # кнопки мыши вроде не лежат в keys
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    self.attack()
                if e.button == 3:
                    self.ulta()
        if keys[pygame.K_w]:
            self.go(0, -1)
        if keys[pygame.K_a]:
            self.go(-1, 0)
        if keys[pygame.K_s]:
            self.go(0, 1)
        if keys[pygame.K_d]:
            self.go(1, 0)
        if keys[pygame.K_e]:
            self.interaction()
        #  self.weapons[0].update(self)
