import pygame # импорт библиотеки pygame
class Laser(): # создание класса "Лазер"
    def __init__(self, screen): # функция инициализации лазера
        self.screen = screen # создание экрана вывода для лазера
        self.image = pygame.image.load('images/лазер.png') # загрузка изображения лазера
        self.rect = self.image.get_rect() # создание прямоугольника в качестве экрана вывода
        self.screen_rect = screen.get_rect() # создание экрана в виде прямоугольника
        self.rect.centerx =float(self.screen_rect.centerx) # привязка координаты x нашего лазера к центру прямоугольника
        self.rect.bottom = self.screen_rect.bottom # привязка координаты y нашего лазера к низу прямоугольника
        self.move_right = False # логическая переменная, отвечающая за движение вправо
        self.move_left = False # логическая переменная, отвечающая за движение влево
    def output(self): # функция вывода лазера на экран
        self.screen.blit(self.image, self.rect) # вывод лазера
    def update_laser(self): # функция обновления позиции лазера
        if self.move_right and self.rect.right < self.screen_rect.right: # если нажата клавиша d и лазер находится не за правой границей, то
            self.rect.centerx += 7.5 # добавляем переменной x 5 единиц
        if self.move_left and self.rect.left > 0: # если нажата клавиша a и лазер находица не за левой границей, то
            self.rect.centerx -= 7.5 # уменьшаем переменную x на 5 единиц