import threading
import time
import random
from queue import Queue


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.que = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            empty_tables = True
            for table in self.tables:
                empty_tables = True
                if table.guest == None:
                    table.guest = guest
                    print(f'{guest.name} сел(а) за стол номер {table.number}')
                    guest.start()
                    guest.join()
                    break
                else:
                    empty_tables = False
            if empty_tables is False:
                self.que.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while self.que.empty() is not True:
            for table in self.tables:
                if table.guest is not None:
                    if table.guest.is_alive() is False:
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        table.guest = None
                        print(f'Стол номер {table.number} свободен')
                if table.guest is None and self.que.empty() is not True:
                    table.guest = self.que.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()
                    table.guest.join()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
