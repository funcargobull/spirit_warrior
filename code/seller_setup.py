import pygame
import weapons
import inspect
from load_images import load_image
from sprites import *
from potions import *

class Text(pygame.sprite.Sprite):
    def __init__(self, character, text, size, color):
        super().__init__(seller_sprites)
        self.character = character
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
    
    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            for item in inspect.getmembers(weapons):
                if str(item[1]).startswith("<class 'weapons."):
                    weapon = eval(f"weapons.{item[0]}()")
                    if self.text == weapon.russian_name:
                        if self.character.money >= weapon.cost:
                            self.character.weapons.append(weapon)
                            self.character.money -= weapon.cost
    
    def clear_all(self):
        self.rect.size = (0, 0)
        self.rect.x = -1000
        self.rect.y = -1000

class Picture(pygame.sprite.Sprite):
    def __init__(self, character, file, pos_x, pos_y, size=None, *groups):
        super().__init__(*groups)
        self.character = character
        self.file = file
        if size is not None:
            self.image = pygame.transform.scale(load_image(self.file), size)
        else:
            self.image = load_image(self.file, 3)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    
    def check_click(self, mouse):
        if self.rect.collidepoint(mouse) and self.file != "pictures/ui/seller_stand.png":
            for item in inspect.getmembers(weapons):
                if str(item[1]).startswith("<class 'weapons."):
                    weapon = eval(f"weapons.{item[0]}()")
                    if weapon.image_ == self.file:
                        if self.character.money >= weapon.cost:
                            self.character.weapons.append(weapon)
                            self.character.money -= weapon.cost
    
    def clear_all(self):
        self.rect.size = (0, 0)
        self.rect.x = -1000
        self.rect.y = -1000

class SellerSetup:
    def __init__(self, character):
        self.character = character
        self.seller_stand = Picture(self.character, "pictures/ui/seller_stand.png", 0, 0, (1000, 730), seller_sprites)
        self.seller_stand.rect.x = 1380 // 2 - self.seller_stand.rect.width // 2
        self.seller_stand.rect.y = 780 // 2 - self.seller_stand.rect.height // 2

        x_pic, y_pic = 272, 191
        for item in inspect.getmembers(weapons):
            if str(item[1]).startswith("<class 'weapons.") and str(item[0]) != "OldPistol": # 582
                weapon = eval(f"weapons.{item[0]}()")
                pic = Picture(self.character, weapon.image_, x_pic, y_pic, None, seller_sprites) # (272, 191)
                text = Text(self.character, weapon.russian_name, 15, (0, 0, 0))
                text.rect.x = pic.rect.x + pic.rect.width + 10
                text.rect.y = pic.rect.y + (pic.rect.height - text.rect.height) // 2

                cost = Text(self.character, str(weapon.cost), 15, (255, 165, 0))
                cost.rect.x = text.rect.x + text.rect.width + 10
                cost.rect.y = text.rect.y
                y_pic += pic.rect.height + 20
                if y_pic >= 562:
                    x_pic += 300
                    y_pic = 191

        small_health = SmallHealthPotion(self.character, 872, 291, 0, 0)
        small_health_cost = Text(self.character, str(small_health.cost), 15, (255, 165, 0))
        small_health_cost.rect.x = small_health.rect.x + small_health.rect.width + 10
        small_health_cost.rect.y = small_health.rect.y + (small_health.rect.height - small_health_cost.rect.height) // 2

        big_health = BigHealthPotion(self.character, small_health_cost.rect.x + small_health_cost.rect.width + 10, small_health.rect.y - 12, 0, 0)
        big_health_cost = Text(self.character, str(big_health.cost), 15, (255, 165, 0))
        big_health_cost.rect.x = big_health.rect.x + big_health.rect.width + 10
        big_health_cost.rect.y = big_health.rect.y + (big_health.rect.height - big_health_cost.rect.height) // 2

        small_energy = SmallEnergyPotion(self.character, small_health.rect.x, small_health.rect.y + small_health.rect.height + 10, 0, 0)
        small_energy_cost = Text(self.character, str(small_energy.cost), 15, (255, 165, 0))
        small_energy_cost.rect.x = small_energy.rect.x + small_energy.rect.width + 10
        small_energy_cost.rect.y = small_energy.rect.y + (small_energy.rect.height - small_energy_cost.rect.height) // 2

        big_energy = BigEnergyPotion(self.character, big_health.rect.x, big_health.rect.y + big_health.rect.height + 10, 0, 0)
        big_energy_cost = Text(self.character, str(big_energy.cost), 15, (255, 165, 0))
        big_energy_cost.rect.x = big_energy.rect.x + big_energy.rect.width + 10
        big_energy_cost.rect.y = big_energy.rect.y + (big_energy.rect.height - big_energy_cost.rect.height) // 2