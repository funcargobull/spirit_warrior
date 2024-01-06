import os.path
import os
import pygame
from choosing_character import *
from new_game import NewGame
from database import Database

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((0, 0))
w, h = pygame.display.get_surface().get_size()
print(w, h)

all_sprites = pygame.sprite.Group()
choosing_character_sprites = pygame.sprite.Group()
frames = pygame.sprite.Group()
walls = pygame.sprite.Group()
tiles = pygame.sprite.Group()

new_game_began = False

# Работа с БД
database = Database()


# Класс текста
class Text(pygame.sprite.Sprite):
    def __init__(self, text, size, color):
        super().__init__(all_sprites)
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


# Весь текст на стартовом окне
game_name = Text("Spirit Warrior", 100, (255, 255, 255))
game_name.rect.x = w // 2 - game_name.rect.width // 2
game_name.rect.y = h // 6

start_game = Text("Новая игра", 70, (255, 255, 215))
start_game.rect.x = w // 2 - start_game.rect.width // 2
start_game.rect.y = game_name.rect.y * 2.5

load_game = Text("Загрузить игру", 70, (196, 196, 189))
load_game.rect.x = w // 2 - load_game.rect.width // 2
load_game.rect.y = game_name.rect.y * 3.5

exit_game = Text("Выход", 70, (252, 76, 73))
exit_game.rect.x = w // 2 - exit_game.rect.width // 2
exit_game.rect.y = game_name.rect.y * 4.5

# Игровой цикл
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            # Начать игру
            if start_game.rect.collidepoint(event.pos):
                for sprite in all_sprites.sprites():
                    sprite.clear_all()
                # Окно выбора персонажа
                choosing_character = ChoosingCharacter(choosing_character_sprites, w, h)
            # Загрузить игру
            if load_game.rect.collidepoint(event.pos):
                pass
            # Выйти
            if exit_game.rect.collidepoint(event.pos):
                if os.path.exists("tmp.txt"):
                    os.remove("tmp.txt")
                running = False
            # Начать игру (окно выбора персонажа)
            try:
                if choosing_character.start_new_game.rect.collidepoint(event.pos) and os.path.exists(
                        "tmp.txt"):
                    for sprite in choosing_character_sprites.sprites():
                        sprite.clear_all()
                    for sprite in frames.sprites():
                        sprite.clear_all()
                    with open("tmp.txt") as f:
                        hero_name = f.read()
                    # Начало новой игры
                    new_game_began = True
                    new_game = NewGame(all_sprites, hero_name, 1)
            except NameError:
                pass

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if os.path.exists("tmp.txt"):
                    os.remove("tmp.txt")
                running = False
        choosing_character_sprites.update(event, frames)

    all_sprites.draw(screen)
    frames.draw(screen)
    choosing_character_sprites.draw(screen)
    if new_game_began:
        new_game.setup(walls, tiles)

    walls.draw(screen)
    tiles.draw(screen)

    pygame.display.flip()
    clock.tick(60)
    print(pygame.mouse.get_pos())

pygame.quit()
