# Lambda-функция
import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))

# Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, 'a+', encoding='utf-8')
        for i in data_set:
            print(i)
            file.write(str(i))
        file = open(file_name, 'r', encoding='utf-8')
        return file.read()
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# __call__
from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words
        self.__call__()

    def __call__(self):
        return random.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())