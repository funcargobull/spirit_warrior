from enemy import Enemy


class Skeleton(Enemy):
    def __init__(self, x, y):
        super().__init__(10, 4, 5, 'picturies/enemyes/enemy08_{}.png', 8, 'faraway', 1000, x, y)


class Crab(Enemy):
    def __init__(self, x, y):
        super().__init__(8, 2, 6, 'picturies/enemyes/enemy30_{}.png', 6, 'nearest', 800, x, y)


class Snowman(Enemy):
    def __init__(self, x, y):
        super().__init__(9, 3, 5, 'picturies/enemyes/enemy34_{}.png', 6, 'faraway', 900, x, y)


class Star(Enemy):
    def __init__(self, x, y):
        super().__init__(12, 3, 5, 'picturies/enemyes/enemy36_{}.png', 6, 'faraway', 1100, x, y)


class EliteMummy(Enemy):
    def __init__(self, x, y):
        super().__init__(25, 6, 7, 'picturies/enemyes/enemy40_{}.png', 6, 'faraway', 1500, x, y)


class FireSpider(Enemy):
    def __init__(self, x, y):
        super().__init__(24, 5, 8, 'picturies/enemyes/enemy41_{}.png', 8, 'nearest', 1200, x, y)


class FireKnight(Enemy):
    def __init__(self, x, y):
        super().__init__(36, 4, 6, 'picturies/enemyes/enemy43_{}.png', 6, 'faraway', 1500, x, y)


class LittleKnight(Enemy):
    def __init__(self, x, y):
        super().__init__(12, 2, 8, 'picturies/enemyes/enemy03_{}.png', 6, 'nearest', 700, x, y)


class UpgradeKnight(Enemy):
    def __init__(self, x, y):
        super().__init__(24, 4, 6, 'picturies/enemyes/enemy04_{}.png', 6, 'faraway', 1500, x, y)


class UpgradeSkeleton(Enemy):
    def __init__(self, x, y):
        super().__init__(20, 4, 6, 'picturies/enemyes/enemy08_{}.png', 8, 'faraway', 1500, x, y)


class EntTree(Enemy):
    def __init__(self, x, y):
        super().__init__(510, 5, 5, 'picturies/enemyes/boss14_new_{}.png', 8, 'stay', 900, x, y, boss=True)


class KingSkeleton(Enemy):
    def __init__(self, x, y):
        super().__init__(720, 5, 8, 'picturies/enemyes/boss03_{}.png', 8, 'faraway', 1000, x, y, boss=True)


class Sangria(Enemy):
    def __init__(self, x, y):
        super().__init__(800, 5, 5, 'picturies/enemyes/bossrush_final_normal_run_{}.png', 11, 'nearest', 900, x, y, boss=True)
