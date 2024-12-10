import multiprocessing
import time
import psutil
import math
from typing import List
import tasks
import sqlite3

cpu = psutil.Process()
names = list()
N_JOBS = 4
LOAD = 100_000_000

rdb = sqlite3.connect('Database/Result.db')
cursor = rdb.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS MultiResults(
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
        m = multiprocessing.Process(target=tasks.write_words, args=(i, f'file{n}.txt'))
        names.append(m)
        m.start()
        n += 1
    for i in range(0, len(names)):
        names[i].join()
    names.clear()
    ended_at = time.time()
    elapsed = round(ended_at - started_at, 6)
    memories = f'{round(cpu.memory_percent(), 6)}%'
    print(f'Время работы: {elapsed} секунд')
    print(f'Нагрузка на память: {memories}%')
    cursor.execute('INSERT or REPLACE INTO MultiResults (task, time, memory) VALUES (?, ?, ?)', (1, f'{elapsed}', f'{memories}'))


def summer(arr: List[int], i: int, summ: List[int]) -> None:
    begin = int(i * LOAD / N_JOBS)
    end = int((i + 1) * LOAD / N_JOBS)
    res = 0
    for k in range(begin, end):
        res += math.sqrt(arr[k])
    summ[i] = res


def task_2():
    started_at = time.time()
    arr = list(range(LOAD))
    processes = [None] * N_JOBS
    with multiprocessing.Manager() as manager:
        summ = manager.list([0] * N_JOBS)
        processes = [None] * N_JOBS
        for i in range(N_JOBS):
            processes[i] = multiprocessing.Process(target=summer, args=(arr, i, summ))
            processes[i].start()
        for i in range(N_JOBS):
            processes[i].join()
        print(f'Резуальтат: {sum(summ)}')
        ended_at = time.time()
    elapsed = round(ended_at - started_at, 6)
    memories = f'{round(cpu.memory_percent(), 6)}%'
    print(f'Время работы: {elapsed} секунд')
    print(f'Нагрузка на память: {memories}%')
    cursor.execute('INSERT or REPLACE INTO MultiResults (task, time, memory) VALUES (?, ?, ?)', (2, f'{elapsed}', f'{memories}'))


"""Задача 3"""


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


def get_conn(host, port):
    """имитация асинхронного соединения с некой периферией"""
    print('Устанавливаем соединение...')
    time.sleep(2)
    print('Соединение установлено.')
    return Conn()


class Connection(multiprocessing.Process):
    """этот конструктор будет выполнен в заголовке with"""
    def __init__(self, host, port):
        super().__init__()
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
        send_task = multiprocessing.Process(target=conn.put_data, args=())
        receive_task = multiprocessing.Process(target=conn.get_data, args=())
        send_task.start()
        receive_task.start()
        send_task.join()
        receive_task.join()
    ended_at = time.time()
    elapsed = round(ended_at - started_at, 6)
    memories = f'{round(cpu.memory_percent(), 6)}%'
    print(f'Время работы: {elapsed} секунд')
    print(f'Нагрузка на память: {memories}%')
    cursor.execute('INSERT or REPLACE INTO MultiResults (task, time, memory) VALUES (?, ?, ?)', (3, f'{elapsed}', f'{memories}'))


"""Задача 4"""


def writer(name, list_t):
    result = open(f'Files/Text_Numbers{name}.txt', 'w+', encoding='utf-8')
    for j in range(0, len(list_t)):
        result.write(f'{tasks.number_to_words(list_t[j])}\n')
    print(f'Запись файла {name} завершена')
    result.close()


def task_4():
    text_list = list()
    started_at = time.time()
    n = -1
    nums = list()
    small_list = list()
    x = '0\n'
    with open('Files/Numbers.txt', encoding='utf-8') as file:
        for line in file.readlines():
            if len(line) > len(x):
                text_list.append(small_list)
                n += 1
                nums.append(n)
                x = line
                small_list = []
            small_list.append(int(line))
        text_list.append(small_list)
        n += 1
        nums.append(n)
    with multiprocessing.Pool(8) as p:
        for i in range(0, len(nums)):
            p.starmap(writer, [(nums[i], text_list[i])])
    ended_at = time.time()
    elapsed = round(ended_at - started_at, 6)
    memories = f'{round(cpu.memory_percent(), 6)}%'
    print(f'Время работы: {elapsed} секунд')
    print(f'Нагрузка на память: {memories}%')
    cursor.execute('INSERT or REPLACE INTO MultiResults (task, time, memory) VALUES (?, ?, ?)', (4, f'{elapsed}', f'{memories}'))


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
        m = multiprocessing.Process(target=gen_res, args=(numBDays[i],))
        names.append(m)
        m.start()
    for name in names:
        name.join()
    names.clear()
    ended_at = time.time()
    elapsed = round(ended_at - started_at, 6)
    memories = f'{round(cpu.memory_percent(), 6)}%'
    print(f'Время работы: {elapsed} секунд')
    print(f'Нагрузка на память: {memories}%')
    cursor.execute('INSERT or REPLACE INTO MultiResults (task, time, memory) VALUES (?, ?, ?)', (5, f'{elapsed}', f'{memories}'))


if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    rdb.commit()
    rdb.close()