import pygame.font
from pygame.sprite import Group
from meteor import Meteor
class Score(): # класс вывода игровой информации
    def __init__(self, screen, stats): # инициализация подсчёта очков
        self.screen = screen # передача значения экрана
        self.screen_rect = screen.get_rect() # передача значения физической части экрана
        self.stats = stats # передача статистики
        self.text_color = (255,255,255) # задание цвета текста
        self.font = pygame.font.SysFont(None, 40) # задание шрифта текста
        self.img_score() # вызов функции рендеринга текста в изображение
        self.lifes = Group() # создание списка жизней
    def img_score(self): # преобразует текст в графику
        self.score_out = self.font.render(str(self.stats.score), True, self.text_color, None) # рендер текста на вывод на экран
        self.score_rect = self.score_out.get_rect() # создание физического объекта счёта
        self.score_rect.left = self.screen_rect.left + 20 # задание положения очков слева
        self.score_rect.top = 20 # задание положения очков сверху
    def show_score(self): # вывод счёта на экран
        self.screen.blit(self.score_out, self.score_rect) # вывод изображения
        self.lifes.draw(self.screen) # отрисовка счёта
    def show_life(self): # функция отображения количества жизней
        self.lifes = Group() # создание списка жизней
        for life_count in range(self.stats.life): # цикл, который отрисовывает количество жизней, в зависимости от того, сколько их осталось
            lif = Meteor(self.screen) # создание изображения жизни на экране
            lif.rect.x = 10 # задание координаты x
            lif.rect.y = 40 + life_count * 50 # задание координаты y
            self.lifes.add(lif) # добавление жизни в список