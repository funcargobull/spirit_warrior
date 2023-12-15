from character import Character


class Knight(Character):
    def __init__(self, x, y, all_sprites, character_sprites):
        super().__init__(5, 5, 200, [], x, y, 'picturies/characters/Knight/knight_0_{}.png', 10, all_sprites,
                         character_sprites)
