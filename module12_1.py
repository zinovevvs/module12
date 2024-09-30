import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def walk(self):
        self.distance += 5

    def run(self):
        self.distance += 6

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner("Тестовый Бегун")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("Тестовый Бегун")
        for y in range(10):
            runner.run()
        self.assertEqual(runner.distance, 60)

    def test_challenge(self):
        runner1 = Runner("Бегун 1")
        runner2 = Runner("Бегун 2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()
