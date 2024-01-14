import pygame
from sprites import *
from load_images import load_image

# зелье
class Potion(pygame.sprite.Sprite):
    def __init__(self, character, file, cost, add_health, add_energy):
        super().__init__(seller_sprites)
        self.character = character
        self.file = file
        self.image = load_image(self.file, 3)
        self.rect = self.image.get_rect()
        self.cost = cost
        self.add_health = add_health
        self.add_energy = add_energy
    
    # клик на зелье и проверка, может ли игрок его купить
    # маленькое зелье здоровья - +2 hp, большое зелье - +4 hp
    # маленькое зелье энергии - +40 энергии, большое зелье - +80 энергии
    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            if self.file.split("_")[0] == "pictures/potions/small" and self.file.split("_")[1] == "health":
                self.add_health = min(self.character.health + 2, self.character.max_health)
            elif self.file.split("_")[0] == "pictures/potions/big" and self.file.split("_")[1] == "health":
                self.add_health = min(self.character.health + 4, self.character.max_health)
            elif self.file.split("_")[0] == "pictures/potions/small" and self.file.split("_")[1] == "energy":
                self.add_energy = min(self.character.energy + 40, self.character.max_energy)
            elif self.file.split("_")[0] == "pictures/potions/big" and self.file.split("_")[1] == "energy":
                self.add_energy = min(self.character.energy + 80, self.character.max_energy)

            if self.character.money >= self.cost:
                if self.file.split("_")[1] == "health":
                    self.character.health = self.add_health
                    self.character.money -= self.cost
                elif self.file.split("_")[1] == "energy":
                    self.character.energy = self.add_energy
                    self.character.money -= self.cost
                
    # очистка спрайта с экрана
    def clear_all(self):
        self.rect.size = (0, 0)
        self.rect.x = -1000
        self.rect.y = -1000


class SmallHealthPotion(Potion):
    def __init__(self, character, x, y, add_health, add_energy):
        super().__init__(character, "pictures/potions/small_health_potion.png",
                         12, add_health, add_energy)
        self.rect.x = x
        self.rect.y = y


class BigHealthPotion(Potion):
    def __init__(self, character, x, y, add_health, add_energy):
        super().__init__(character, "pictures/potions/big_health_potion.png",
                         25, add_health, add_energy)
        self.rect.x = x
        self.rect.y = y


class SmallEnergyPotion(Potion):
    def __init__(self, character, x, y, add_health, add_energy):
        super().__init__(character, "pictures/potions/small_energy_potion.png",
                         12, add_health, add_energy)
        self.rect.x = x
        self.rect.y = y


class BigEnergyPotion(Potion):
    def __init__(self, character, x, y, add_health, add_energy):
        super().__init__(character, "pictures/potions/big_energy_potion.png",
                         25, add_health, add_energy)
        self.rect.x = x
        self.rect.y = y
