import threading
import time
import psutil
import math
from typing import List
import tasks
import sqlite3

lock = threading.Lock()
cpu = psutil.Process()
threads_list = list()
N_JOBS = 4
LOAD = 100_000_000

rdb = sqlite3.connect('Database/Result.db')
cursor = rdb.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS ThreadsResults(
task INTEGER NOT NULL PRIMARY KEY,
time FLOAT NOT NULL,
memory TEXT NOT NULL
)
''')


"""Задача 1"""


def task_1():
    started_at = time.time()
    n = 0
    for i in range(1000000, 500000, -100000):
        x = threading.Thread(target=tasks.write_words, args=(i, f'file{n}.txt'))
        threads_list.append(x)
        x.start()
        n += 1
    for i in range(0, len(threads_list)):
        threads_list[i].join()
    threads_list.clear()
    ended_at = time.time()
    elapsed = round(ended_at - started_at, 6)
    memories = f'{round(cpu.memory_percent(), 6)}%'
    print(f'Время работы: {elapsed} секунд')
    print(f'Нагрузка на память: {memories}%')
    cursor.execute('INSERT or REPLACE INTO ThreadsResults (task, time, memory) VALUES (?, ?, ?)', (1, f'{elapsed}', f'{memories}'))


"""Задача 2"""


def summer(arr: List[int], i: int, summ: List[int], lock: threading.Lock) -> None:
    begin = int(i * LOAD / N_JOBS)
    end = int((i + 1) * LOAD / N_JOBS)
    res = 0
    for k in range(begin, end):
        res += math.sqrt(arr[k])
    with lock:
        summ[i] = res


def task_2():
    started_at = time.time()
    arr = list(range(LOAD))
    summ = [0] * N_JOBS
    threads = [None] * N_JOBS
    for i in range(N_JOBS):
        threads[i] = threading.Thread(target=summer, args=(arr, i, summ, lock))
        threads[i].start()
    for i in range(N_JOBS):
        threads[i].join()
    print(f'Резуальтат: {sum(summ)}')
    ended_at = time.time()
    elapsed = round(ended_at - started_at, 6)
    memories = f'{round(cpu.memory_percent(), 6)}%'
    print(f'Время работы: {elapsed} секунд')
    print(f'Нагрузка на память: {memories}%')
    cursor.execute('INSERT or REPLACE INTO ThreadsResults (task, time, memory) VALUES (?, ?, ?)', (2, f'{elapsed}', f'{memories}'))


"""Задача 3"""


def get_conn(host, port):
    """имитация асинхронного соединения с некой периферией"""
    class Conn:
        def put_data(self):
            print('Отправка данных...')
            time.sleep(2)
            print('Данные отправлены.')

        def get_data(self):
            print('Получение данных...')
            time.sleep(2)
            print('Данные получены.')

        def close(self):
            print('Завершение соединения...')
            time.sleep(2)
            print('Соединение завершено.')

    print('Устанавливаем соединение...')
    time.sleep(2)
    print('Соединение установлено.')
    return Conn()


class Connection:
    """этот конструктор будет выполнен в заголовке with"""
    def __init__(self, host, port):
        self.host = host
        self.port = port

    """ этот метод будет неявно выполнен при входе в with"""
    def __enter__(self):
        self.conn = get_conn(self.host, self.port)
        return self.conn

    """ этот метод будет неявно выполнен при выходе из with"""
    def __exit__(self, exc_type, exc, tb):
        self.conn.close()


def task_3():
    started_at = time.time()
    with Connection('localhost', 9001) as conn:
        send_task = threading.Thread(target=conn.put_data, args=())
        receive_task = threading.Thread(target=conn.get_data, args=())
        send_task.start()
        receive_task.start()
        send_task.join()
        receive_task.join()
    ended_at = time.time()
    elapsed = round(ended_at - started_at, 6)
    memories = f'{round(cpu.memory_percent(), 6)}%'
    print(f'Время работы: {elapsed} секунд')
    print(f'Нагрузка на память: {memories}%')
    cursor.execute('INSERT or REPLACE INTO ThreadsResults (task, time, memory) VALUES (?, ?, ?)', (3, f'{elapsed}', f'{memories}'))


"""Задача 4"""


def task_4():
    started_at = time.time()
    text_list = list()
    small_list = list()
    x = '0\n'
    n = 0
    with open('Files/Numbers.txt', encoding='utf-8') as file:
        for line in file.readlines():
            if len(line) > len(x):
                text_list.append(small_list)
                n += 1
                x = line
                small_list = []
            small_list.append(int(line))
        text_list.append(small_list)
        n += 1

    def writer(name):
        result = open(f'Files/Text_Numbers{name}.txt', 'w+', encoding='utf-8')
        for j in range(0, len(text_list[name])):
            result.write(f'{tasks.number_to_words(text_list[name][j])}\n')
        print(f'Запись файла {name} завершена')
        result.close()

    for num in range(0, n):
        t = threading.Thread(target=writer, args=(num,))
        threads_list.append(t)
        t.start()
    for thread in threads_list:
        thread.join()
    threads_list.clear()
    ended_at = time.time()
    elapsed = round(ended_at - started_at, 6)
    memories = f'{round(cpu.memory_percent(), 6)}%'
    print(f'Время работы: {elapsed} секунд')
    print(f'Нагрузка на память: {memories}%')
    cursor.execute('INSERT or REPLACE INTO ThreadsResults (task, time, memory) VALUES (?, ?, ?)', (4, f'{elapsed}', f'{memories}'))


"""Задача 5"""


# Генерируем и отображаем дни рождения:
def gen_res(numBDays):
    print(f'В списке {numBDays} дней рождений:')
    birthdays = tasks.get_birthdays(numBDays)
    # Выясняем, встречаются ли два совпадающих дня рождения.
    match = tasks.get_match(birthdays)
    # Отображаем результаты:
    if match is not None:
        month_name = tasks.months[match.month - 1]
        date_text = f'{match.day} {month_name}'
        print(f'В этой симуляции несколько человек родились {date_text}')
    else:
        print(f'В этой симуляции нет человек с совпадающим днём рождения.')
    # Производим 1000000 операций имитационного моделирования:
    print(f'Генерация {numBDays} случайных дней рождений 1,000,000 раз...')
    sim_match = 0  # Число операций моделирования с совпадающими днями рождения.
    for i in range(1_000_000):
        if tasks.get_match(tasks.get_birthdays(numBDays)) is not None:
            sim_match = sim_match + 1
    # Отображаем результаты имитационного моделирования:
    probability = round(sim_match / 1_000_000 * 100, 2)
    print(f'Из 1,000,000 симуляций в группе из {numBDays} людей совпадают дни рождения {sim_match} раз. Таким образом, {numBDays} с шансом {probability}% будут иметь совпадающие дни рождения.')

def task_5():
    started_at = time.time()
    numBDays = list()
    for i in range(2, 101, 14):
        numBDays.append(i)
    for i in range(0, len(numBDays)):
        t = threading.Thread(target=gen_res, args=(numBDays[i],))
        threads_list.append(t)
        t.start()
    for thread in threads_list:
        thread.join()
    threads_list.clear()
    ended_at = time.time()
    elapsed = round(ended_at - started_at, 6)
    memories = f'{round(cpu.memory_percent(), 6)}%'
    print(f'Время работы: {elapsed} секунд')
    print(f'Нагрузка на память: {memories}%')
    cursor.execute('INSERT or REPLACE INTO ThreadsResults (task, time, memory) VALUES (?, ?, ?)', (5, f'{elapsed}', f'{memories}'))


task_1()
task_2()
task_3()
task_4()
task_5()
rdb.commit()
rdb.close()