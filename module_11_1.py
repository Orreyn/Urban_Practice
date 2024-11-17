from PIL import Image, ImageFilter
import requests
import numpy


class Numbs:
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.list = numpy.random.randint(0, 21, (a, b)) # создание матрицы a на b со случайными целыми значениями от 0 до 20

    def powers(self, n): # возвращает матрицу в степени, если матрица квадратная (т.е. у неё одинаковое количество строк и столбцов)
        if self.a == self.b:
            result = numpy.linalg.matrix_power(self.list, n)
            return print(f'{result}')
        else:
            return print(f'Матрица не является квадратной, операция невозможна')

    def min_max(self):
        list_min, list_max = self.list.min(), self.list.max()
        return print(f'Минимальное значение матрицы: {list_min}.\nМаксимальное значение матрицы: {list_max}') # функция выводит наименьшее и наиболее значение в матрице

    def mat_rev(self):
        rev_list = numpy.flip(self.list)
        return print(f'{rev_list}') # функция полностью переворачивает элементы в матрице - первый становится последний, второй предпоследним и т.д.


nump1 = Numbs(2, 3)
print(nump1.list)
nump1.powers(2) # возведение в степень не сработает - матрица не квадратная
nump1.min_max()
nump1.mat_rev()

nump2 = Numbs(4, 4)
print(nump2.list)
nump2.powers(2) # возведение в степень сработает
nump2.min_max()
nump2.mat_rev()


class Reqs:
    req = None

    def req_get(self, name):
        if isinstance(name, str) is False:
            name = str(name)
        self.req = requests.get(name) # функция получает ссылку и приравнивает к ней переменную, которая в дальнейшем используется для вызова всех остальных действий
        return self.req

    def info(self):
        x = str
        print(requests.models.Response.ok)
        if self.req.status_code == 200: # изменяет, что именно функция будет выдавать о работоспособности сайта - вместо <Response [200]> будет выдавать 'OK' и т.д.
            x = 'OK'
        elif self.req.status_code == 400:
            x = 'Bad Request'
        elif self.req.status_code == 403:
            x = 'Forbidden'
        elif self.req.status_code == 404:
            x = 'Not Found'
        elif self.req.status_code == 500:
            x = 'Internal Server Error'
        elif self.req.status_code == 502:
            x = 'Bad Gateway'
        return print(f'Ссылка: {self.req.url}\nСостояние: {x}\nЗаголовки: {self.req.headers}\n')


r = Reqs()
r.req_get('https://github.com/Orreyn/Urban_Practice/tree/main')
r.info()


class Pillow:
    def __init__(self, name):
        self.name = name
        self.img = None
        self.img_open() # выхов функции открытия, чтобы переменная считалась открытой сразу после создания класса

    def img_open(self):
        self.img = Image.open(self.name) # функция создаёт переменную с открытой картинкой
        return self.img

    def img_show(self):
        return self.img.show() # Отображение картинки

    def full_rotate(self, name):
        img_gif_list = list()
        for i in range(36):
            x = self.img.rotate(10) # Поворот картинки на 10 градусов 36 раз - по итогу получается полный круг
            img_gif_list.append(x)
        img_gif_list[0].save(name, save_all=True,  append_images=img_gif_list[1:], optimize=True, duration=100, loop=0) # все 36 элементов списка сохраняются в гифку, которой мы указываем имя при создании функции
        img_gif = Image.open(name)
        return img_gif.show()


    def img_bw(self):
        bw = self.img.convert('L')
        bw = bw.filter(ImageFilter.SMOOTH).filter(ImageFilter.FIND_EDGES) # функция возвращает чёрно-белый вариант картинки, где все контуры - белые, а всё остальное - чёрное
        return bw.show()


ball = Pillow('pokeball.png')
ball.img_show()
ball.full_rotate('pokeball.gif') # почему-то гифка не работает, но я так и не поняла, почему
ball.img_bw()