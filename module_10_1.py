import threading
import time


def write_words(word_count, file_name):
    file = open(file_name, 'w+', encoding='utf-8')
    for i in range(word_count+1):
        file.write(f'Какое-то слово №{i}\n')
        time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


started_at = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
ended_at = time.time()
elapsed = round(ended_at - started_at, 6)
print(f'Работа потоков {elapsed}',)

started_at1 = time.time()
t5 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
t5.start()

t6 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
t6.start()

t7 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
t7.start()

t8 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
t8.start()

t5.join()
t6.join()
t7.join()
t8.join()
ended_at1 = time.time()
elapsed1 = round(ended_at1 - started_at1, 6)
print(f'Работа потоков {elapsed1}',)
