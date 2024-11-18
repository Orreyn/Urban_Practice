import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        tw = Runner('Ходун')
        for i in range(10):
            tw.walk()
        self.assertEqual(tw.distance, 50)

    def test_run(self):
        tr = Runner('Бегун')
        for i in range(10):
            tr.run()
        self.assertEqual(tr.distance, 100)

    def test_challenge(self):
        tw = Runner('Ходун')
        tr = Runner('Бегун')
        for i in range(10):
            tw.walk()
        for i in range(10):
            tr.run()
        self.assertNotEqual(tr.distance, tw.distance)

if __name__ == '__main__':
    unittest.main()
