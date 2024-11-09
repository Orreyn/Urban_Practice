class Vehicle:
    __COLOR_VARIANTS = ['black', 'white', 'silver', 'red', 'blue', 'yellow']

    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return print(f'Модель: {self.__model}')

    def get_horsepower(self):
        return print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        return print(f'Цвет: {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        return print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        for i in range(0, len(self.__COLOR_VARIANTS)):
            if new_color.lower() == self.__COLOR_VARIANTS[i]:
                self.__color = new_color
                break
        if new_color.lower() != self.__color.lower():
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['black', 'white', 'silver', 'red', 'blue', 'yellow']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()