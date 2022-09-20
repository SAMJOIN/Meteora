from stats import Stats
from laser import Laser # импорт класса Laser
import pygame, controls # импорт библиотеки pygame
from pygame.sprite import Group # импорт класса Group
from meteor import Meteor # импорт класса Meteor
from score import Score
def run(): # функция работы игры
    pygame.init() # инициализация библиотеки
    screen = pygame.display.set_mode((1000,800)) # создание рабочего экрана
    pygame.display.set_caption("Meteora") # создание заголовка игры
    background = pygame.image.load('images/фон.png') # загрузка изображения с фоном
    laser = Laser(screen) # переменная лазера + вызов класса лазера
    bullets = Group() # создания списка с пулями
    meteor = Meteor(screen) # создание метеора
    stats = Stats() # создание таблицы статистики
    score = Score(screen, stats) # создание таблицы счёта
    while True: # бесконечный цикл
        if stats.alive: # если есть жизни
            controls.events(screen, laser, bullets) # вызов функции обработки событий
            laser.update_laser() # вызов функции обновления позиции лазера
            controls.screen_update(background, screen, stats, score, laser, meteor, bullets) # вызов функции отрисовки экрана, лазера и пуль
            controls.update_bullets(meteor, bullets)  # вызов функции обновления пуль
            controls.update_meteor(meteor, stats, score) # вызов функции обновления метеора
            controls.collision(meteor, bullets, stats, score) # вызов функции обработки столкновения пули и метеорита
        else: # иначе
            controls.events(screen, laser, bullets) # обрабатываем события
            controls.screen_update(background, screen, laser, meteor, bullets) # отрисовываем объекты на экране
run() # запуск функции run()