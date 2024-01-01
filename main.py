import pygame
from characters import *
from weapons import *
character_sprites = pygame.sprite.Group()
location_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
weapons_sprites = pygame.sprite.Group()
character = Knight(250, 250, all_sprites, character_sprites)
saber = Saber(weapons_sprites, all_sprites)
character.weapons = [saber, saber]
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((198 * 3, 108 * 3))
    screen.fill((0, 0, 0))
    fps = 30
    running = True
    clock = pygame.time.Clock()
    pos = (0, 0)
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                pos = event.pos
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # чтобы выйти можно было нормально
                    running = False
        screen.fill((255, 255, 255))
        character_sprites.update(events, pos)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
