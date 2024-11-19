import unittest
import tests_12_3 as t12

tester = unittest.TestSuite()
tester.addTest(unittest.TestLoader().loadTestsFromTestCase(t12.RunnerTest))
tester.addTest(unittest.TestLoader().loadTestsFromTestCase(t12.TournamentTest))

ttr = unittest.TextTestRunner(verbosity=2)
ttr.run(tester)