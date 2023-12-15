import pygame
from characters import *
character_sprites = pygame.sprite.Group()
location_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
weapons_sprites = pygame.sprite.Group()
'''пресонаж и должен следовать за положением мышки, ибо туда он будет стрелять
управляется клавишами w, s, a, d. Кнопки мыши пока не работают, лучше их не нажимать). Рваную анимацию я потом починю'''
character = Knight(250, 250, all_sprites, character_sprites)
if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
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
        screen.fill((255, 255, 255))
        character_sprites.update(events, pos)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
