from weapon import Weapon


class Saber(Weapon):
    def __init__(self, weapon_sprites, all_sprites):
        super().__init__(4, 2, str, 15, 'picturies/weapons/weapons_62.png', 0, 15, weapon_sprites, all_sprites)
