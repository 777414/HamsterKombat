import pygame
import utils
import json
from datetime import datetime

pygame.init()
with open(r"data\score.json") as fp:
    score = json.load(fp)

# окно
WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

icon = pygame.image.load(r"imgs\logo_icon.png")
coin = pygame.image.load(r"imgs\dollar.png").convert_alpha()
coin = pygame.transform.smoothscale(coin, (32,32))
price_coin = pygame.transform.smoothscale(coin, (32,32))
button = pygame.image.load(r"imgs\button.png").convert_alpha()
button = pygame.transform.smoothscale(button, (400,400))
logo_coin = pygame.image.load(r"imgs\logo_coin.png").convert_alpha()
logo_coin = pygame.transform.smoothscale(logo_coin, (200,200))
button_mult = pygame.image.load(r"imgs\upgrade.png") .convert_alpha()
button_mult = pygame.transform.smoothscale(button_mult, (100,100))

pygame.display.set_icon(icon)
pygame.display.set_caption("Hamster Kombat")
background = pygame.Surface((WIDTH, HEIGHT))
utils.draw_vertical_gradient(background, (0, 0, 0), (10, 10, 40))

# цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# счётчик кликов
clicks = score["score"]
CLICK_DURATION = 150
click_time = 0
price_mult = score["price"]

# шрифт
font = pygame.font.Font(None, 48)

# игровой цикл
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            score["last_exit"] = datetime.now().timestamp()
            score["score"] = clicks
            with open("data\score.json", "w") as fp:
                fp.write(json.dumps(score, indent=4))
            running = False

        # если кликнули мышкой
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicks += 1
            click_time = pygame.time.get_ticks()

    pressed = pygame.time.get_ticks() - click_time < CLICK_DURATION

    screen.fill(WHITE)

    text = font.render(f"{clicks}", True, WHITE)
    mult = font.render(f"X{score['mult']}", True, WHITE)
    price = font.render(f"{price_mult}", True, WHITE)
    screen.blit(background, (0, 0))
    screen.blit(text, (100, 550))
    screen.blit(mult, (50, 50))
    screen.blit(coin, (50,549))

    if pressed:
        dark_button = button.copy()
        dark_button.fill((0, 0, 0, 60), special_flags=pygame.BLEND_RGBA_SUB)
        screen.blit(dark_button, (10, 100 + 3))
        dark_logo_button = logo_coin.copy()
        dark_logo_button.fill((0, 0, 0, 60), special_flags=pygame.BLEND_RGBA_SUB)
        screen.blit(dark_logo_button, (110, 190 + 3))
    else:
        screen.blit(button, (10, 100))
        screen.blit(logo_coin, (110, 190))

    screen.blit(button_mult, (280,15))
    screen.blit(price, (305,105))
    screen.blit(price_coin, (270, 105))

    pygame.display.update()

pygame.quit()