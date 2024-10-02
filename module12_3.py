import unittest
from test_12_3 import RunnerTest, TournamentTest

test_suite = unittest.TestSuite()
test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

# Создание объекта TextTestRunner с verbosity=2
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)

