import pygame
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
w, h = pygame.display.get_surface().get_size()


class Text:
    def __init__(self, text, size, color):
        self.text = text
        self.size = size
        self.color = color
        self.font_skeleton = pygame.font.Font(
            "code/pixeleum.ttf", self.size).render(self.text, False, self.color)
        self.rect = self.font_skeleton.get_rect()

    def draw(self):
        screen.blit(self.font_skeleton, (self.rect.x, self.rect.y))


running = True

# Весь текст
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
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if start_game.rect.collidepoint(event.pos):
                start_game.font_skeleton = pygame.font.Font(
                    "code/pixeleum.ttf", start_game.size).render(start_game.text, False, (153, 144, 142))
                print("GAME STARTED")
            if load_game.rect.collidepoint(event.pos):
                pass
            if exit_game.rect.collidepoint(event.pos):
                running = False
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if start_game.rect.collidepoint(event.pos):
                start_game.font_skeleton = pygame.font.Font(
                    "code/pixeleum.ttf", start_game.size).render(start_game.text, False, (255, 255, 215))

    screen.fill((0, 0, 0))
    game_name.draw()
    start_game.draw()
    load_game.draw()
    exit_game.draw()

    pygame.display.flip()
pygame.quit()
