import pygame
from characters import *
from weapons import *
from sprites import *

character = Knight(250, 250)
character.weapons = [Machete(), LaserGun()]
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
                    character.health -= 1
        screen.fill((255, 255, 255))
        print(character.energy)
        character_sprites.update(events, pos)
        bullet_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
