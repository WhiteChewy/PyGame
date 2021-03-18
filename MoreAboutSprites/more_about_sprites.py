# Скеллет игрового цикла в Pygame
import pygame
import random
import os


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # инициализация встроенного класса Sprite
        # любой спрайт в pygame должен иметь свойства image и rect
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()  # rect - это сокращенное от rectangle
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.move = 1

    # метод update определяет движение объекта
    def update(self):
        self.rect.x += self.move*5
        if self.rect.right >= WIDTH:
            self.move = -1
        elif self.rect.left <= 0:
            self.move = 1


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
# настройка папки assets
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'assets')
player_img = pygame.image.load(os.path.join(img_folder, 'p1_jump.png')).convert()

all_sprites = pygame.sprite.Group()  # группировка спрайтов в одну группу
player = Player()
all_sprites.add(player)


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
    all_sprites.update()

    # Рендеринг
    screen.fill(BLUE)  # заливка окна черным
    all_sprites.draw(screen)
    pygame.display.flip()  # отображение отрисованного экрана

pygame.quit()
