from enemy import Enemy


class Skeleton(Enemy):
    def __init__(self, x, y):
        super().__init__(10, 3, 2, 'pictures/enemies/enemy08_{}.png', 8, 'faraway', 1200, x, y)


class Crab(Enemy):
    def __init__(self, x, y):
        super().__init__(8, 2, 3, 'pictures/enemies/enemy30_{}.png', 6, 'nearest', 800, x, y)


class Snowman(Enemy):
    def __init__(self, x, y):
        super().__init__(9, 3, 3, 'pictures/enemies/enemy34_{}.png', 6, 'faraway', 900, x, y)


class Star(Enemy):
    def __init__(self, x, y):
        super().__init__(20, 3, 3, 'pictures/enemies/enemy36_{}.png', 6, 'faraway', 1100, x, y)


class EliteMummy(Enemy):
    def __init__(self, x, y):
        super().__init__(25, 6, 4, 'pictures/enemies/enemy40_{}.png', 6, 'faraway', 1500, x, y)


class FireSpider(Enemy):
    def __init__(self, x, y):
        super().__init__(24, 5, 5, 'pictures/enemies/enemy41_{}.png', 8, 'nearest', 1200, x, y)


class FireKnight(Enemy):
    def __init__(self, x, y):
        super().__init__(36, 4, 4, 'pictures/enemies/enemy43_{}.png', 6, 'faraway', 1500, x, y)


class LittleKnight(Enemy):
    def __init__(self, x, y):
        super().__init__(12, 2, 5, 'pictures/enemies/enemy03_{}.png', 6, 'nearest', 700, x, y)


class UpgradeKnight(Enemy):
    def __init__(self, x, y):
        super().__init__(24, 4, 3, 'pictures/enemies/enemy04_{}.png', 6, 'faraway', 1500, x, y)


class UpgradeSkeleton(Enemy):
    def __init__(self, x, y):
        super().__init__(20, 4, 4, 'pictures/enemies/enemy08_{}.png', 8, 'faraway', 1500, x, y)


class EntTree(Enemy):
    def __init__(self, x, y):
        super().__init__(300, 3, 3, 'pictures/enemies/boss14_new_{}.png',
                         8, 'stay', 1200, x, y, boss=True)


class KingSkeleton(Enemy):
    def __init__(self, x, y):
        super().__init__(400, 5, 2, 'pictures/enemies/boss03_{}.png',
                         8, 'faraway', 1200, x, y, boss=True)


class Sangria(Enemy):
    def __init__(self, x, y):
        super().__init__(500, 5, 3, 'pictures/enemies/bossrush_final_normal_run_{}.png', 11, 'nearest', 1000, x, y,
                         boss=True)
