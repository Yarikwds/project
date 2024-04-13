import pygame
import sys
import time
import menu

# Инициализация Pygame
pygame.init()

# Установка параметров экрана
WIDTH, HEIGHT = 800, 600
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)

# Загрузка изображений
coin_img = pygame.image.load('coin.png')
coin_img = pygame.transform.scale(coin_img, (50, 50))

upgrade_button_img = pygame.image.load('upgrade_button.png')
upgrade_button_img = pygame.transform.scale(upgrade_button_img, (150, 50))

speed_button_img = pygame.image.load('speed_button.png')
speed_button_img = pygame.transform.scale(speed_button_img, (150, 50))

close_button_img = pygame.image.load('close_button.png')
close_button_img = pygame.transform.scale(close_button_img, (30, 30))

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Генератор монет")

# Параметры игрока
coins = 0
coins_per_second = 1

# Параметры магазина
upgrade_cost = 10
speed_cost = 50
upgrade_multiplier = 2

# Шрифты
font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 24)
big_font = pygame.font.SysFont(None, 72)

# Функция отображения магазина
def draw_shop():
    pygame.draw.rect(screen, BLACK, (WIDTH - 200, 0, 200, HEIGHT))
    shop_text = font.render("Магазин", True, WHITE)
    screen.blit(shop_text, (WIDTH - 180, 10))
    screen.blit(upgrade_button_img, (WIDTH - 180, 50))
    screen.blit(speed_button_img, (WIDTH - 180, 120))
    screen.blit(close_button_img, (WIDTH - 40, 10))
    
    # Подписи под кнопками
    upgrade_text = small_font.render(f"Улучшение (x{upgrade_multiplier} монет/сек) - {upgrade_cost} монет", True, WHITE)
    screen.blit(upgrade_text, (WIDTH - 180, 100))
    
    speed_text = small_font.render(f"Увеличить скорость (1 монета) - {speed_cost} монет", True, WHITE)
    screen.blit(speed_text, (WIDTH - 180, 170))

# Функция отображения текущего количества монет
def draw_coins():
    coins_text = font.render("Монеты: " + str(coins), True, BLACK)
    screen.blit(coins_text, (20, 20))
    screen.blit(coin_img, (20, 50))

# Функция покупки улучшения
def buy_upgrade(cost):
    global coins_per_second, coins, upgrade_cost, speed_cost, upgrade_multiplier
    if coins >= cost:
        coins -= cost
        if cost == upgrade_cost:
            coins_per_second *= upgrade_multiplier
            upgrade_cost *= upgrade_multiplier
        elif cost == speed_cost:
            coins_per_second += 1

# Основной цикл игры
def main_game():
    running = True
    clock = pygame.time.Clock()
    last_time = time.time()

    while running:
        screen.fill(WHITE)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Обновление монет
        current_time = time.time()
        if current_time - last_time >= 1:
            global coins
            coins += coins_per_second
            last_time = current_time

        # Отображение компонентов игры
        draw_coins()
        draw_shop()

        # Обновление экрана
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    if menu.main_menu():
        main_game()

pygame.quit()
sys.exit()
