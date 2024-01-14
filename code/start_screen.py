import os.path
import os
import pygame
from choosing_character import *
from new_game import NewGame
from database import Database
from sprites import *
from characters import *
from weapons import *
from seller_setup import SellerSetup

pygame.init()
pygame.font.init()

# БД
database = Database()

screen = pygame.display.set_mode((1380, 780))
pygame.display.set_caption("Spirit Warrior")
pygame.display.set_icon(pygame.image.load(
    'pictures/characters/Assassin/assassin_0_0.png'))
w, h = pygame.display.get_surface().get_size()

walls_and_tiles = pygame.Surface((w, h))

new_game_began = False


# Класс текста
class Text(pygame.sprite.Sprite):
    def __init__(self, text, size, color, *groups):
        super().__init__(*groups)
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
game_name = Text("Spirit Warrior", 100, (255, 255, 255), all_sprites)
game_name.rect.x = w // 2 - game_name.rect.width // 2
game_name.rect.y = h // 6

start_game = Text("Новая игра", 70, (255, 255, 215), all_sprites)
start_game.rect.x = w // 2 - start_game.rect.width // 2
start_game.rect.y = game_name.rect.y * 2.5

load_game = Text("Загрузить игру", 70, (196, 196, 189), all_sprites)
load_game.rect.x = w // 2 - load_game.rect.width // 2
load_game.rect.y = game_name.rect.y * 3.5

exit_game = Text("Выход", 70, (252, 76, 73), all_sprites)
exit_game.rect.x = w // 2 - exit_game.rect.width // 2
exit_game.rect.y = game_name.rect.y * 4.5

game_over = Text("Проигрыш", 70, (255, 0, 0), game_over_sprites)
game_over.rect.x = w // 2 - game_over.rect.width // 2
game_over.rect.y = h // 2 - game_over.rect.height // 2

game_win = Text("Победа", 70, (0, 255, 0), game_win_sprites)
game_win.rect.x = w // 2 - game_win.rect.width // 2
game_win.rect.y = h // 2 - game_win.rect.height // 2

# Игровой цикл
running = True
clock = pygame.time.Clock()
pos = (0, 0)

while running:
    screen.fill((0, 0, 0))
    events = pygame.event.get()
    keys = pygame.key.get_pressed()

    for event in events:
        if event.type == pygame.QUIT:
            if os.path.exists("tmp.txt"):
                os.remove("tmp.txt")
            running = False
        if event.type == pygame.MOUSEMOTION:
            pos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            for s in seller_sprites:
                s.check_click(event.pos)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            # Начать игру
            if start_game.rect.collidepoint(event.pos):
                for sprite in all_sprites.sprites():
                    sprite.clear_all()
                # Окно выбора персонажа
                choosing_character = ChoosingCharacter(choosing_character_sprites)
            # Загрузить игру
            if load_game.rect.collidepoint(event.pos):
                try:
                    hero_name, wave, weapons, money = database.get_data()
                    character = eval(f"{hero_name}(1380 // 2, 780 // 2)")
                    character.weapons = []
                    for weapon in weapons.split(";"):
                        character.weapons.append(eval(f"{weapon}()"))
                    character.money = money
                    character.gaming = True
                    new_game = NewGame(character, wave)
                    new_game.setup()
                    new_game.start_wave()
                    new_game_began = True
                except IndexError:
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
                    character = eval(f"{hero_name}(1380 // 2, 780 // 2)")
                    character.weapons = [OldPistol()]
                    database.fill_data(hero_name, 1, "OldPistol", 0)
                    character.gaming = True
                    new_game = NewGame(character, database.get_wave())
                    new_game.setup()
                    new_game.start_wave()
                    new_game_began = True
            except NameError:
                pass

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if os.path.exists("tmp.txt"):
                    os.remove("tmp.txt")
                running = False
            if event.key == pygame.K_e:
                if new_game_began:
                    # взаимодействие с торговцем
                    if pygame.sprite.spritecollideany(character, seller):
                        character.on_sell = not character.on_sell
                        seller_setup = SellerSetup(character)

        choosing_character_sprites.update(event, frames)

    all_sprites.draw(screen)
    frames.draw(screen)
    choosing_character_sprites.draw(screen)

    if new_game_began and character.health > 0 and character.gaming:
        screen.blit(walls_and_tiles, (0, 0))

        walls.draw(screen)
        tiles.draw(screen)
        location_sprites.draw(screen)
        enemy_sprites.draw(screen)
        character_sprites.draw(screen)

        for w in weapons_sprites:
            if w == character.weapons[0]:
                w.draw(screen)
        character_sprites.draw(screen)
        bullet_sprites.draw(screen)

        ui_sprites.draw(screen)

        new_game.update()

        # пауза игры, когда идет взаимодействие с торговцем
        if not character.on_sell:
            for s in seller_sprites:
                s.clear_all()
            character_sprites.update(events, pos)
            bullet_sprites.update(character)
            enemy_sprites.update(character)
        else:
            seller_sprites.draw(screen)
    
    try:
        if character.health <= 0:
            new_game_began = False
            character.gaming = False
            game_over_sprites.draw(screen)

            for s in all_sprites:
                all_sprites.remove(s)
            for s in choosing_character_sprites:
                choosing_character_sprites.remove(s)
        if character.wave == 16:
            new_game_began = False
            character.gaming = False
            game_win_sprites.draw(screen)

            for s in all_sprites:
                all_sprites.remove(s)
            for s in choosing_character_sprites:
                choosing_character_sprites.remove(s)

    except NameError:
        pass

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
