import pygame
import utils

pygame.init()

# окно
WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.Surface((WIDTH, HEIGHT))
utils.draw_vertical_gradient(background, (0, 0, 0), (10, 10, 40))

# цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# счётчик кликов
clicks = 0

# шрифт
font = pygame.font.Font(None, 48)

# игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # если кликнули мышкой
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicks += 1

    screen.fill(WHITE)
    screen.blit(background, (0, 0))

    text = font.render(f"{clicks}", True, WHITE)
    screen.blit(background, (0, 0))
    screen.blit(text, (100, 550))

    pygame.display.update()

pygame.quit()