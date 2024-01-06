from weapon import Weapon


class Machete(Weapon):
    def __init__(self):
        super().__init__(6, 1, 'sword', 600, 'pictures/weapons/weapons_62.png', 0, 20, 10)


class OldPistol(Weapon):
    def __init__(self):
        super().__init__(3, 0.5, 'gun', 500, 'pictures/weapons/weapons_19.png', 0, 10, 10)


class Eagle(Weapon):
    def __init__(self):
        super().__init__(4, 1, 'gun', 400, 'pictures/weapons/weapons_22.png', 1, 15, 10)


class P250(Weapon):
    def __init__(self):
        super().__init__(3, 0.5, 'gun', 500, 'pictures/weapons/weapons_28.png', 0, 10, 10)


class AK(Weapon):
    def __init__(self):
        super().__init__(3, 0.5, 'gun', 150, 'pictures/weapons/weapons_21.png', 1, 17, 10)


class SnowFox(Weapon):
    def __init__(self):
        super().__init__(2, 0.5, 'gun', 150, 'pictures/weapons/weapons_10.png', 0, 20, 10)


class M4(Weapon):
    def __init__(self):
        super().__init__(4, 0.5, 'gun', 150, 'pictures/weapons/weapons_35.png', 1, 25, 10)


class PPM1(Weapon):
    def __init__(self):
        super().__init__(5, 0.7, 'gun', 100, 'pictures/weapons/weapons_118.png', 3, 35, 13)


class PPNEW1(Weapon):
    def __init__(self):
        super().__init__(2, 0.5, 'gun', 80, 'pictures/weapons/weapons2_122.png', 1, 40, 13)


class Aurora(Weapon):
    def __init__(self):
        super().__init__(16, 1, 'gun', 900, 'pictures/weapons/weapons_2.png', 6, 50, 15)


class ShoutGun(Weapon):
    def __init__(self):
        super().__init__(4, 2, 'gun', 600, 'pictures/weapons/weapons_37.png', 2, 20, 7)


class MachineGun(Weapon):
    def __init__(self):
        super().__init__(3, 1, 'gun', 100, 'pictures/weapons/weapons_s_06.png', 1, 70, 13)


class Rapira(Weapon):
    def __init__(self):
        super().__init__(6, 1, 'sword', 400, 'pictures/weapons/weapons_57.png', 0, 20, 10)


class LightSaber(Weapon):
    def __init__(self):
        super().__init__(8, 1, 'sword', 350, 'pictures/weapons/weapons_109.png', 0, 35, 10)


class Axe(Weapon):
    def __init__(self):
        super().__init__(10, 1, 'sword', 400, 'pictures/weapons/weapons3_3.png', 0, 25, 10)


class AxeSnow(Weapon):
    def __init__(self):
        super().__init__(9, 1, 'sword', 400, 'pictures/weapons/weapons5_52.png', 0, 40, 10)


class SwordNinja(Weapon):
    def __init__(self):
        super().__init__(10, 1, 'sword', 400, 'pictures/weapons/weapons_ninja.png', 0, 60, 10)


class LaserGun(Weapon):
    def __init__(self):
        super().__init__(15, 2, 'gun', 1000, 'pictures/weapons/weapons3_168.png', 4, 80, 20)
