class Stats(): # класс для отслеживания статистики
    def __init__(self): # инициализация статистики
        self.reset_stats() # обновление статистики
        self.alive = True # переменная, отвечающая за то, что жизни ещё есть
    def reset_stats(self): # функция обновления статистики
        self.life = 3 # начальное количество жизней
        self.score = 0 # начальное количество очков