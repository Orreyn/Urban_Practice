import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name, self.power = name, power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        days = 0
        while enemies > 0:
            time.sleep(1)
            enemies += -self.power
            if enemies < 0:
                enemies = 0
            days += 1
            print(f'{self.name} сражается {days}-й день, осталось {enemies} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


king = Knight('Король Артур', 30)
leo = Knight('Сэр Леон', 10)
king.start()
leo.start()
king.join()
leo.join()

print('Все битвы закончились!')