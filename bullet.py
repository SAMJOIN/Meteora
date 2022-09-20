import pygame # импорт библиотеки pygame
class Bullet(pygame.sprite.Sprite): # создание класса "Пуля"
    def __init__(self, screen, laser): # функция инициализации пули
        super(Bullet, self).__init__() # использование инициализатора супер класса
        self.screen = screen # подгрузка экрана
        self.rect = pygame.Rect(0, 0, 2, 20) # создание спрайта пули
        self.color = 0, 162, 232 # задание цвета пули
        self.speed = 15 # установка скорости пули
        self.rect.centerx = laser.rect.centerx # начальная координата x пули
        self.rect.top = laser.rect.top +50 # начальная координата y пули
        self.y = self.rect.y # собственная координата y пули
    def update(self): # функция для перемещения пули вверх
        self.y -= self.speed # уменьшаем координату y на значение скорости
        self.rect.y = self.y # устанавливаем значение спрайта пули на новую координату
    def draw_bullet(self): # функция для отрисовки пули на экране
        pygame.draw.rect(self.screen, self.color, self.rect) # отрисовка пули