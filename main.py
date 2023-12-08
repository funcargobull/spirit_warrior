import pygame
character_sprites = pygame.sprite.Group()
location_sprites = pygame.sprite.Group()
if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    fps = 30
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
