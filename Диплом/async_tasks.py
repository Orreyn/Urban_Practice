import asyncio
import time
import psutil
import math
from typing import List
import tasks
import sqlite3

cpu = psutil.Process()
N_JOBS = 4
LOAD = 100_000_000
lock = asyncio.Lock()

rdb = sqlite3.connect('Database/Result.db')
cursor = rdb.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS asyncResults(
task INTEGER NOT NULL PRIMARY KEY,
time FLOAT NOT NULL,
memory TEXT NOT NULL
)
''')


async def ticker(fr, to, step=1):
    """Функция, которая создаёт циклы в ассинхронных функциях"""
    for i in range(fr, to, step):
        yield i


"""Задача 1"""


async def task_1():
    n = 0
    async for i in ticker(1000000, 500000, -100000):
        tasks.write_words(i, f'file{n}.txt')
        n += 1


started_at = time.time()
asyncio.run(task_1())
ended_at = time.time()
elapsed = round(ended_at - started_at, 6)
memories = f'{round(cpu.memory_percent(), 6)}%'
print(f'Время работы: {elapsed} секунд')
print(f'Нагрузка на память: {memories}%')
cursor.execute('INSERT or REPLACE INTO asyncResults (task, time, memory) VALUES (?, ?, ?)', (1, f'{elapsed}', f'{memories}'))


"""Задача 2"""


async def summer(arr: List[int], i: int, summ: List[int]) -> None:
    begin = int(i * LOAD / N_JOBS)
    end = int((i + 1) * LOAD / N_JOBS)
    res = 0
    async for k in ticker(begin, end):
        res += math.sqrt(arr[k])
    summ[i] = res


async def task_2():
    arr = list(range(LOAD))
    summ = [0] * N_JOBS
    result = [None] * N_JOBS
    async for i in ticker(0, N_JOBS):
        result[i] = await summer(arr, i, summ)
    print(f'Резуальтат: {sum(summ)}')


started_at = time.time()
asyncio.run(task_2())
ended_at = time.time()
elapsed = round(ended_at - started_at, 6)
memories = f'{round(cpu.memory_percent(), 6)}%'
print(f'Время работы: {elapsed} секунд')
print(f'Нагрузка на память: {memories}%')
cursor.execute('INSERT or REPLACE INTO asyncResults (task, time, memory) VALUES (?, ?, ?)', (2, f'{elapsed}', f'{memories}'))


"""Задача 3"""


async def get_conn(host, port):
    """имитация асинхронного соединения с некой периферией"""
    class Conn:
        async def put_data(self):
            print('Отправка данных...')
            await asyncio.sleep(2)
            print('Данные отправлены.')

        async def get_data(self):
            print('Получение данных...')
            await asyncio.sleep(2)
            print('Данные получены.')

        async def close(self):
            print('Завершение соединения...')
            await asyncio.sleep(2)
            print('Соединение завершено.')

    print('Устанавливаем соединение...')
    await asyncio.sleep(2)
    print('Соединение установлено.')
    return Conn()


class Connection:
    """этот конструктор будет выполнен в заголовке with"""
    def __init__(self, host, port):
        self.host = host
        self.port = port

    """ этот метод будет неявно выполнен при входе в with"""
    async def __aenter__(self):
        self.conn = await get_conn(self.host, self.port)
        return self.conn

    """ этот метод будет неявно выполнен при выходе из with"""
    async def __aexit__(self, exc_type, exc, tb):
        await self.conn.close()


async def main():
    async with Connection('localhost', 9001) as conn:
        send_task = asyncio.create_task(conn.put_data())
        receive_task = asyncio.create_task(conn.get_data())

        """операции отправки и получения данных выполняются конкурентно"""
        await send_task
        await receive_task


started_at = time.time()
asyncio.run(main())
ended_at = time.time()
elapsed = round(ended_at - started_at, 6)
memories = f'{round(cpu.memory_percent(), 6)}%'
print(f'Время работы: {elapsed} секунд')
print(f'Нагрузка на память: {memories}%')
cursor.execute('INSERT or REPLACE INTO asyncResults (task, time, memory) VALUES (?, ?, ?)', (3, f'{elapsed}', f'{memories}'))


"""Задача 4"""


async def task_4():

    text_list = list()
    small_list = list()
    x = '0\n'
    n = 0
    with open('Files/Numbers.txt', encoding='utf-8') as file:
        lines = file.readlines()
        async for line in ticker(0, len(lines)):
            if len(lines[line]) > len(x):
                text_list.append(small_list)
                n += 1
                x = lines[line]
                small_list = []
            small_list.append(int(lines[line]))
        text_list.append(small_list)
        n += 1

    async def writer(name):
        result = open(f'Files/Text_Numbers{name}.txt', 'w+', encoding='utf-8')
        async for j in ticker(0, len(text_list[name])):
            result.write(f'{tasks.number_to_words(text_list[name][j])}\n')
        print(f'Запись файла {name} завершена')
        result.close()

    async for num in ticker(0, n):
        await writer(num)


started_at = time.time()
asyncio.run(task_4())
ended_at = time.time()
elapsed = round(ended_at - started_at, 6)
memories = f'{round(cpu.memory_percent(), 6)}%'
print(f'Время работы: {elapsed} секунд')
print(f'Нагрузка на память: {memories}%')
cursor.execute('INSERT or REPLACE INTO asyncResults (task, time, memory) VALUES (?, ?, ?)', (4, f'{elapsed}', f'{memories}'))


"""Задача 5"""


# Генерируем и отображаем дни рождения:
async def gen_res(numBDays):
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
    async for i in ticker(0, 1_000_000):
        if tasks.get_match(tasks.get_birthdays(numBDays)) is not None:
            sim_match = sim_match + 1
    # Отображаем результаты имитационного моделирования:
    probability = round(sim_match / 1_000_000 * 100, 2)
    print(f'Из 1,000,000 симуляций в группе из {numBDays} людей совпадают дни рождения {sim_match} раз. Таким образом, {numBDays} с шансом {probability}% будут иметь совпадающие дни рождения.')

async def task_5():
    numBDays = list()
    async for i in ticker(2, 101, 14):
        numBDays.append(i)
    async for i in ticker(0, len(numBDays)):
        await gen_res(numBDays[i])


started_at = time.time()
asyncio.run(task_5())
ended_at = time.time()
elapsed = round(ended_at - started_at, 6)
memories = f'{round(cpu.memory_percent(), 6)}%'
print(f'Время работы: {elapsed} секунд')
print(f'Нагрузка на память: {memories}%')
cursor.execute('INSERT or REPLACE INTO asyncResults (task, time, memory) VALUES (?, ?, ?)', (5, f'{elapsed}', f'{memories}'))

rdb.commit()
rdb.close()
