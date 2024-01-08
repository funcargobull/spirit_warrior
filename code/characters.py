import pygame.time

from character import Character


class Knight(Character):
    def __init__(self, x, y):
        super().__init__(6, 5, 180, [], x, y, 'pictures/characters/Knight/knight_0_{}.png', 5, 20, 20)

    def ulta(self):
        """восстанавливает 3 еденицы брони"""
        time_action, time = 15000, pygame.time.get_ticks()
        if self.ulta_tick + time_action < time:
            self.armor = min(self.armor + 3, self.max_armor)
            self.ulta_tick = time


class Assassin(Character):
    def __init__(self, x, y):
        super().__init__(4, 4, 180, [], x, y, 'pictures/characters/Assassin/assassin_0_{}.png', 6, 20, 20)

    def ulta(self):
        """восстанавливает 30 едениц енергии"""
        time_action, time = 15000, pygame.time.get_ticks()
        if self.ulta_tick + time_action < time:
            self.energy = min(self.energy + 30, self.max_energy)
            self.ulta_tick = time


class Priest(Character):
    def __init__(self, x, y):
        super().__init__(3, 5, 200, [], x, y, 'pictures/characters/Priest/priest_0_{}.png', 5, 20, 20)

    def ulta(self):
        """восстанавливает 1 еденицу здоровья"""
        time_action, time = 15000, pygame.time.get_ticks()
        if self.ulta_tick + time_action < time:
            self.health = min(self.health + 1, self.max_health)
            self.ulta_tick = time
