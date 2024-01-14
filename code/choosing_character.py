import pygame
from load_images import load_image


# Рамка вокруг персонажа при его выборе
class Frame(pygame.sprite.Sprite):
    def __init__(self, group, color, x, y, width, height):
        super().__init__(group)
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height), 1)
        self.rect.x = x
        self.rect.y = y

    # Очистка спрайтов с экрана
    def clear_all(self):
        self.rect.size = (0, 0)
        self.rect.x = -1000
        self.rect.y = -1000


# Класс картинки героя
class Hero(pygame.sprite.Sprite):
    def __init__(self, group, file, pos, size):
        super().__init__(group)
        self.file = file
        self.image = pygame.transform.scale(load_image(self.file), size)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            # Создание белой рамки вокруг персонажа при клике
            if args[1]:
                args[1].remove(args[1].sprites())
                Frame(args[1], (255, 255, 255), *self.rect.topleft, self.rect.width, self.rect.height)
            else:
                Frame(args[1], (255, 255, 255), *self.rect.topleft, self.rect.width, self.rect.height)
            # Внесение в файл tmp.txt названия выбранного героя (Assassin, Knight, Priest)
            with open("tmp.txt", "w") as f:
                f.write(self.file.split("/")[2])

    # Очистка спрайтов с экрана
    def clear_all(self):
        self.rect.size = (0, 0)
        self.rect.x = -1000
        self.rect.y = -1000


# Класс текста
class Text(pygame.sprite.Sprite):
    def __init__(self, group, text, size, color):
        super().__init__(group)
        self.text = text
        self.size = size
        self.color = color
        self.font = pygame.font.Font("pixeleum.ttf", self.size)
        self.textSurf = self.font.render(self.text, False, self.color)
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image = pygame.Surface((W, H))
        self.rect = self.image.get_rect()
        self.image.blit(self.textSurf, (self.rect.x, self.rect.y))

    # Очистка спрайтов с экрана
    def clear_all(self):
        self.rect.size = (0, 0)
        self.rect.x = -1000
        self.rect.y = -1000


# Основной класс окна с выбором персонажаs
class ChoosingCharacter:
    def __init__(self, group, width=1380, height=780):
        self.group = group

        self.main_text = Text(self.group, "Выберите персонажа", 80, (255, 255, 255))
        self.main_text.rect.x = width // 2 - self.main_text.rect.width // 2
        self.main_text.rect.y = height // 30

        self.assassin_sprite = Hero(
            self.group, "pictures/characters/Assassin/assassin_0_0.png", (0, 0), (145, 140))
        self.assassin_sprite.rect.x = self.main_text.rect.x + self.main_text.rect.width // 4
        self.assassin_sprite.rect.y = self.main_text.rect.y + self.assassin_sprite.rect.height + 20

        self.assassin_text = Text(self.group, "Ассасин", 50, (255, 255, 255))
        self.assassin_text.rect.x = self.assassin_sprite.rect.x - (
                self.assassin_text.rect.width - self.assassin_sprite.rect.width) // 2
        self.assassin_text.rect.y = self.assassin_sprite.rect.y + self.assassin_sprite.rect.height

        self.knight_sprite = Hero(
            self.group, "pictures/characters/Knight/knight_0_0.png", (0, 0), (170, 140))
        self.knight_sprite.rect.x = width - self.assassin_sprite.rect.x - self.assassin_sprite.rect.width
        self.knight_sprite.rect.y = self.assassin_sprite.rect.y

        self.knight_text = Text(self.group, "Рыцарь", 50, (255, 255, 255))
        self.knight_text.rect.x = self.knight_sprite.rect.x - (
                self.knight_text.rect.width - self.knight_sprite.rect.width) // 2
        self.knight_text.rect.y = self.knight_sprite.rect.y + self.knight_sprite.rect.height

        self.priest_sprite = Hero(
            self.group, "pictures/characters/Priest/priest_0_0.png", (0, 0), (135, 155))
        self.priest_sprite.rect.x = (self.assassin_text.rect.bottomright[0] + self.knight_text.rect.bottomleft[
            0]) // 2 - self.priest_sprite.rect.width // 2
        self.priest_sprite.rect.y = self.assassin_text.rect.bottomright[1]

        self.priest_text = Text(self.group, "Священник", 50, (255, 255, 255))
        self.priest_text.rect.x = self.priest_sprite.rect.x - (
                self.priest_text.rect.width - self.priest_sprite.rect.width) // 2
        self.priest_text.rect.y = self.priest_sprite.rect.y + self.priest_sprite.rect.height

        self.start_new_game = Text(self.group, "Начать", 42, (255, 0, 0))
        self.start_new_game.rect.x = self.priest_text.rect.x + (
                self.priest_text.rect.width - self.start_new_game.rect.width) // 2
        self.start_new_game.rect.y = height - self.start_new_game.rect.height
