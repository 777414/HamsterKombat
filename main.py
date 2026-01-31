import pygame
import utils

pygame.init()

# окно
WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
icon = pygame.image.load(r"imgs\logo_icon.png")
coin = pygame.image.load(r"imgs\dollar.png").convert_alpha()
coin = pygame.transform.smoothscale(coin, (32,32))
button = pygame.image.load(r"imgs\button.png").convert_alpha()
button = pygame.transform.smoothscale(button, (400,400))

pygame.display.set_icon(icon)
pygame.display.set_caption("Hamster Kombat")
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

    screen.blit(button, (10, 100))
    screen.blit(coin, (50, 549))
    screen.blit(text, (100, 550))

    pygame.display.update()

pygame.quit()