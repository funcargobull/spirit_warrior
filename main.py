import pygame
from characters import *
from weapons import *
from sprites import *
from enemyes import *

character = Priest(250, 250)
character.weapons = [SwordNinja(), LaserGun()]
Crab(100, 100)
EntTree(150, 150)
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
        # все спрайты отрисовывать не нужно, ибо будет отображаться второе оружие персонажа,
        # а в update почти у каждого класса разные параметры на вход)
        character_sprites.update(events, pos)
        bullet_sprites.update()
        enemy_sprites.update(character)
        location_sprites.draw(screen)
        enemy_sprites.draw(screen)
        character_sprites.draw(screen)
        for w in weapons_sprites:
            if w == character.weapons[0]:
                w.draw(screen)
        bullet_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
