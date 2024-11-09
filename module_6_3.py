from random import randint


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if dz >= 0:
            self._cords[0] = self._cords[0] + dx * self.speed
            self._cords[1] = self._cords[1] + dy * self.speed
            self._cords[2] = self._cords[2] + dz * self.speed
        else:
            print(f'It\'s too deep, i can\'t dive :(')

    def get_cords(self):
        return print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        print(f'Sorry, i\'m peaceful :)') if self._DEGREE_OF_DANGER < 5 else print(
            f'Be careful, i\'m attacking you 0_0')

    def speak(self):
        if self.sound is not None:
            print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        return print(f'Here are(is) {randint(1, 4)} eggs for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] = self._cords[2] - (dz * self.speed) // 2


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
