class Figure:
    sides_count = 0
    perim = 0

    def __init__(self, sides: list[int], __color: list[int], filled=False):
        self.sides = sides
        self.__color = __color
        self.filled = filled
        self.is_valid_color()
        self.is_valid_sides()

    def is_valid_color(self):
        if len(self.__color) > 3:
            del self.__color[4:]
            print(f'Все значения после {self.__color[2]} были удалены, поскольку не соответсвуют формату RGB')
        for i in range(0, len(self.__color)):
            if self.__color[i] < 0 or self.__color[i] > 255:
                print(f'Некорректные значения RGB, цвет сброшен')
                self.__color = [0, 0, 0]

    def get_color(self):
        return print(f'R: {self.__color[0]}, G: {self.__color[1]}, B: {self.__color[2]}')

    def set_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            new_color = self.__color
            self.__color = [r, g, b]
            if new_color == self.__color:
                print(f'Вы ввели тот же цвет')
                return self.__color
            self.is_valid_color()
            if new_color != [0, 0, 0] and self.__color == [0, 0, 0]:
                self.__color = new_color
                print(f'Восстановлен предыдущий цвет')
                return self.__color

    def is_valid_sides(self):
        if isinstance(self.sides, int):
            t = [self.sides]
            self.sides = t
        x = True
        if len(self.sides) > self.sides_count:
            del self.sides[self.sides_count:]
            print(f'Все значения после {self.sides[self.sides_count-1]} были удалены, поскольку у фигуры нет такого количества сторон')
        elif len(self.sides) < self.sides_count:
            if len(self.sides) == 1 and self.sides_count > 1:
                print(f'Фигура считается равносторонней, все стороны равны {self.sides[0]}')
                self.sides = [self.sides[0]]*self.sides_count
            elif len(self.sides) == 0:
                return print(f'Вы не указали никаких сторон, список пуст')
            else:
                print(f'В связи с тем, что значений недостаточно, остальные стороны были приравнены к 1')
                one = [1]
                one = one * (self.sides_count - len(self.sides))
                self.sides.extend(one)
        for i in range(0, len(self.sides)):
            if self.sides[i] <= 0:
                self.sides[i] = None
                x = False
        if x is True:
            print(f'Все значения корректны')
            return self.sides
        else:
            print(f'Среди значений найдены некорректные данные, все неподходящие параметры стали недействительными')

    def get_sides(self):
        return print(f'Стороны: {self.sides}')

    def set_sides(self, *new_sides):
        new_sides = list(new_sides)
        if isinstance(new_sides[0], list):
            new_sides = new_sides[0]
        if len(new_sides) == self.sides_count or len(new_sides) == 1:
            x = self.sides
            self.sides = new_sides
            self.is_valid_sides()
            if len(new_sides) == 1 and self.sides_count > 1:
                new_sides = new_sides * self.sides_count
            if new_sides == self.sides:
                return self.sides
            else:
                self.sides = x
                print(f'Восстановлены предыдущие значения')
                return self.sides
        else:
            print(f'Введено некорректное количество сторон, значения не были приняты. Правильное количество сторон: {self.sides_count}')

    def __len__(self):
        for i in range(0, self.sides_count):
            self.perim += self.sides[i]
        return print(f'Периметр: {self.perim}')


class Circle(Figure):
    sides_count = 1

    def __init__(self, sides: list[int], __color: list[int]):
        super().__init__(sides, __color)
        self.sides = sides
        self.__color = __color
        if isinstance(self.sides, int):
            t = [self.sides]
            self.sides = t
        self.__radius = self.sides[0] / 6.28

    def get_radius(self):
        return print(f'Радиус: {round(self.__radius, 2)}, целочисленный: {int(round(self.__radius, 0))}')

    def get_square(self):
        s = 3.14 * (round(self.__radius, 0) ** 2)
        return print(f'Площадь круга: {round(s, 2)}, целочисленная: {int(round(s, 0))}')


class Triangle(Figure):
    sides_count = 3

    def __init__(self, sides: list[int], __color: list[int]):
        super().__init__(sides, __color)
        self.sides = sides
        self.__color = __color
        if isinstance(self.sides, int):
            t = [self.sides]
            self.sides = t

    def get_square(self):
        p = self.perim // 2
        s = (p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2])) ** 0.5
        return print(f'Площадь треугольника: {round(s, 2)}, целочисленная: {int(round(s, 0))}')


class Cube(Figure):
    sides_count = 12

    def __init__(self, sides: list[int], __color: list[int]):
        super().__init__(sides, __color)
        self.sides = sides
        self.__color = __color
        if isinstance(self.sides, int):
            t = [self.sides]
            self.sides = t

    def is_valid_sides(self):
        x = True
        if self.sides[0] <= 0:
            self.sides[0] = None
            x = False
        if x is True:
            print(f'Значение корректно')
        else:
            print(f'Значение некорректно и было изменено на недействительное')
        if len(self.sides) > 1:
            del self.sides[1:]
            print(f'Все значения после {self.sides[0]} были удалены - куб допустим только равносторонний')
        elif len(self.sides) == 1:
            self.sides = [self.sides[0]]*self.sides_count
            if len(self.sides) == 0:
                return print(f'Вы не указали никаких сторон, список пуст')

    def set_sides(self, *new_sides):
        new_sides = list(new_sides)
        if isinstance(new_sides[0], list):
            new_sides = new_sides[0]
        if new_sides[0] > 0:
            self.sides = new_sides
            self.is_valid_sides()
            return self.sides
        else:
            print(
                f'Введено некорректное значение, изменение не внесено')

    def get_volume(self):
        v = self.sides[0]**3
        return print(f'Объём куба: {round(v, 2)}, целочисленный: {int(round(v, 0))}')


circle1 = Circle(10, [200, 200, 100]) # (стороны и цвет)
triangle1 = Triangle([3, 6, 5], [100, 154, 34])
cube1 = Cube([6, 4, 5], [222, 35, 130])

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
circle1.get_color()
cube1.set_color(300, 70, 15) # Не изменится
cube1.get_color()

# Проверка на изменение сторон:
cube1.set_sides(-5, 3, 12, 4, 5) # Не изменится
cube1.get_sides()
circle1.set_sides(15) # Изменится
circle1.get_sides()

# Проверка периметра (круга), это и есть длина:
circle1.__len__()

# Проверка на радиус и площадь круга
circle1.get_radius()
circle1.get_square()

#Проверка на периметр и площадь треугольника
triangle1.__len__()
triangle1.get_square()

# Проверка объёма (куба):
cube1.get_volume()