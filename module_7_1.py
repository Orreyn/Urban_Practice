class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        print(file.read())
        file.close()

    def add(self, *products):
        file = open(self.__file_name, 'a')
        for i in range(0, len(products)):
            x = True
            s = str(products[i])
            file = open(self.__file_name, 'r')
            if s in str(file.read()):
                x = False
                print(f'Продукт {s} уже есть в магазине')
            else:
                x = True
            file = open(self.__file_name, 'a')
            if x is True:
                file.write(s)
                file.write('\n')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

s1.get_products()