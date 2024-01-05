import pygame.time

from character import Character


class Knight(Character):
    def __init__(self, x, y):
        super().__init__(6, 5, 180, [], x, y, 'picturies/characters/Knight/knight_0_{}.png', 10, 20, 20)

    def ulta(self, key='character_interaction'):
        time_action, time = 3000, pygame.time.get_ticks()
        if (self.ulta_tick + time_action < time) and key == 'character_interaction':
            self.ulta_data = [w.damage for w in self.weapons]
            self.ulta_tick = time
        else:
            for w in self.weapons:
                w.damage //= 2


class Assassin(Character):
    def __init__(self, x, y):
        super().__init__(4, 4, 180, [], x, y, 'picturies/characters/Assasin/assassin_0_{}.png', 15, 20, 20)

    def ulta(self, key='character_interaction'):
        time_action, time = 3000, pygame.time.get_ticks()
        if (self.ulta_tick + time_action < time) and key == 'character_interaction':
            self.ulta_tick = time
        elif self.ulta_tick + time_action >= time:
            self.health = self.max_health


class Priest(Character):
    def __init__(self, x, y):
        super().__init__(3, 5, 200, [], x, y, 'picturies/characters/Priest/priest_0_{}.png', 10, 20, 20)

    def ulta(self, key='character_interaction'):
        time_action, time = 3000, pygame.time.get_ticks()
        if (self.ulta_tick + time_action < time) and key == 'character_interaction':
            self.health = min(self.health + 1, self.max_health)
            self.ulta_tick = time
