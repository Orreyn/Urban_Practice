import multiprocessing
import time


def read_info(name):
    all_data = list()
    file = open(name, 'r')
    for line in file:
        all_data.append(file.readline())


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный
started_at = time.time()
for name in filenames:
    read_info(name)
ended_at = time.time()
elapsed = round(ended_at - started_at, 6)
print(f'{elapsed}')

# Многопроцессный
started_at1 = time.time()
if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
        pool.close()
ended_at1 = time.time()
elapsed1 = round(ended_at1 - started_at1, 6)
print(f'{elapsed1}')

# я не знаю почему он считает время 5 раз, таймеры не попадают в циклы