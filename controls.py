import time
import pygame, sys # импорт библиотек pygame и sys
from stats import Stats
from bullet import Bullet # импорт класса "Пуля"
def events(screen, laser, bullets): # функция обработки событий
    for event in pygame.event.get():  # обработка событий, получаемых игрой
        if event.type == pygame.QUIT:  # если нажат крестик
            sys.exit()  # выход из игры
        elif event.type == pygame.KEYDOWN: # если нажата кнопка
            if event.key == pygame.K_d: # и это клваиша "d"
                laser.move_right = True # двигаем лазер вправо
            elif event.key == pygame.K_a: # если нажата клавиша a
                laser.move_left = True # устанавливаем значение перемещения влево, как истина
            elif event.key == pygame.K_SPACE: # если нажат пробел
                new_bullet = Bullet(screen, laser) # создаём новую пулю
                bullets.add(new_bullet) # добавляем пулю в список всех пуль на экране
        elif event.type == pygame.KEYUP: # иначе, если кнопка не нажата
            if event.key == pygame.K_d: # если не нажата d
                laser.move_right = False # лазер не двигается
            elif event.key == pygame.K_a: # если клавиша a отжата
                laser.move_left = False # перестаём перемещаться влево
def screen_update(background, screen, stats, score, laser, meteor, bullets): # функция обновления объектов, которые выводятся на экран
    screen.blit(background, (0, -200))  # заливка фона
    score.show_score() # вывод счёта
    for bullet in bullets.sprites(): # отрисовка каждой пули в группе bullets
        bullet.draw_bullet() # отрисовка пули
    laser.output()  # отрисовка лазера
    meteor.draw() # отрисовка метеорита
    score.show_life() # отрисовка количества жизней
    pygame.display.flip()  # обновление дисплея
def update_bullets(meteor, bullets): # функция обновления позиций пули и удаления пуль, при достижении края рабочей области
    bullets.update() # функция обновления пули
    for bullet in bullets.copy(): # перебор всех пуль в списке
        if bullet.rect.bottom <= 0: # если пуля достигла верхнего края, то
            bullets.remove(bullet) # удаляем пулю
def update_meteor(meteor, stats, score): # функция обновления метеора
    if stats.life > 0: # если жизней больше, чем 0
        meteor.update() # обновляем кадр метеора
        if meteor.rect.top >= 1000: # если метеор выходит за рамку
            meteor.move() # перемещаем метеор на верх
            stats.life -= 1 # уменьшение жизней
            score.show_life() # отображение жизней
    else: # иначе
        stats.alive = False # говорим, что жизни закончены, а значит мы не живы
        time.sleep(1) # ожидаем немного
        sys.exit() # закрываем игру
def collision(meteor, bullets, stats, score): # функция обработки сбивания пулей метеора
    for bullet in bullets: # перебираем все выстрелившие пули
        if (meteor.rect.x + 70 > bullet.rect.centerx > meteor.rect.x + 40) and (meteor.y +40 > bullet.rect.top > meteor.y): # если координата x и y метеора совпадают с координатой x и y пули, то
            meteor.move() # перемещаем метеор
            bullets.remove(bullet) # удаляем пулю
            stats.score += 1 # добавляем очко
            score.img_score() # прорисовываем таблицу очков
            score.show_life() # отображаем количество жизней