# Скеллет игрового цикла в Pygame
import pygame
import random


# блок определения размеров окна и фпс
WIDTH = 360  # Ширина игрового окна
HEIGHT = 480  # высота игровго окна
FPS = 30  # частота кадров в секунду
# RGB ЦВЕТА
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# далее инициализируется игра и окно
pygame.init()   # "запуск pygame"
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # создание окна игры
pygame.display.set_caption("My game")
clock = pygame.time.Clock()

# игровой цикл
running = True
while running:
    clock.tick(FPS)  # держим цикл на правильной скорости.
    # Обработка событий
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False

    # Обновление

    # Рендеринг
    screen.fill(BLACK)  # заливка окна черным
    pygame.display.flip()  # отображение отрисованного экрана

pygame.quit()
