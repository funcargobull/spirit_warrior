import pygame

def load_image(fullname, colorkey=None):
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

class Frame(pygame.sprite.Sprite):
    def __init__(self, group, color, x, y, width, height):
        super().__init__(group)
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height), 1)
        self.rect.x = x
        self.rect.y = y

class Hero(pygame.sprite.Sprite):
    def __init__(self, group, file, pos, size):
        super().__init__(group)
        self.image = pygame.transform.scale(load_image(file), size)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            if args[1]:
                args[1].remove(args[1].sprites())
                Frame(args[1], (255, 255, 255), *self.rect.topleft, self.rect.width, self.rect.height)
            else:
                Frame(args[1], (255, 255, 255), *self.rect.topleft, self.rect.width, self.rect.height)


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


def choosing_character(screen, group, width, height):
    main_text = Text(group, "Выберите персонажа", 100, (255, 255, 255))
    main_text.rect.x = width // 2 - main_text.rect.width // 2
    main_text.rect.y = height // 6

    assassin_text = Text(group, "Ассасин", 50, (255, 255, 255))
    assassin_text.rect.x = width // 3
    assassin_text.rect.y = height // 2

    assassin_sprite = Hero(
        group, "pictures/characters/Assassin/assassin_0_0.png", (0, 0), (145, 140))
    assassin_sprite.rect.x = assassin_text.rect.x + assassin_sprite.rect.width // 4
    assassin_sprite.rect.y = assassin_text.rect.y - assassin_sprite.rect.height

    knight_text = Text(group, "Рыцарь", 50, (255, 255, 255))
    knight_text.rect.x = width - width // 3 - assassin_text.rect.width
    knight_text.rect.y = height // 2

    knight_sprite = Hero(
        group, "pictures/characters/Knight/knight_0_0.png", (0, 0), (170, 140))
    knight_sprite.rect.x = knight_text.rect.x + knight_sprite.rect.width // 14
    knight_sprite.rect.y = knight_text.rect.y - knight_sprite.rect.height

    priest_sprite = Hero(
        group, "pictures/characters/Priest/priest_0_0.png", (0, 0), (135, 155))
    priest_sprite.rect.x = assassin_text.rect.bottomright[0] + \
        priest_sprite.rect.width // 14
    priest_sprite.rect.y = assassin_text.rect.bottomright[1] + \
        priest_sprite.rect.height // 3

    priest_text = Text(group, "Священник", 50, (255, 255, 255))
    priest_text.rect.x = priest_sprite.rect.bottomleft[0] - \
        priest_text.rect.width // 3.5
    priest_text.rect.y = priest_sprite.rect.y + priest_sprite.rect.height