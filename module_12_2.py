import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        max_speed = 0
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    if participant.speed > max_speed:
                        if place == 1:
                            finishers[place] = participant.name
                            place += 1
                            self.participants.remove(participant)
                        elif place > 1:
                            finishers[place] = finishers[place-1]
                            finishers[place-1] = participant.name
                            place += 1
                            self.participants.remove(participant)
                        max_speed = participant.speed
                    else:
                        finishers[place] = participant.name
                        place += 1
                        self.participants.remove(participant)
        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        return cls.all_results

    @classmethod
    def setUp(cls):
        cls.us = Runner('Усэйн', 10)
        cls.an = Runner('Андрей', 9)
        cls.ni = Runner('Ник', 3)
        return cls.us, cls.an, cls.ni

    @classmethod
    def tearDownClass(cls):
        for i in range(1, len(TournamentTest.all_results)+1):
            print(TournamentTest.all_results[str(i)])

    def test_1(self):
        t1 = Tournament(90, TournamentTest.us, TournamentTest.ni)
        TournamentTest.all_results['1'] = t1.start()
        self.assertTrue(TournamentTest.all_results['1'][2] == TournamentTest.ni.name)

    def test_2(self):
        t2 = Tournament(90, TournamentTest.an, TournamentTest.ni)
        TournamentTest.all_results['2'] = t2.start()
        self.assertTrue(TournamentTest.all_results['2'][2] == TournamentTest.ni.name)

    def test_3(self):
        t3 = Tournament(90, TournamentTest.an, TournamentTest.ni, TournamentTest.us)
        TournamentTest.all_results['3'] = t3.start()
        self.assertTrue(TournamentTest.all_results['3'][3] == TournamentTest.ni.name)


if __name__ == '__main__':
    unittest.main()
