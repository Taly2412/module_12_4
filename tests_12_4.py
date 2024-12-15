import logging
import unittest
from rt_with_exceptions import Runner


class RunnerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                            encoding='UTF-8', format='%(asctime)s | %(levelname)s | %(message)s')

    def test_walk(self):
        try:
            self.runner_1 = Runner('1', -3)
            for _ in range(10):
                self.runner_1.walk()
                logging.info(f'"test_walk" выполнен успешно')

        except ValueError as err:
            logging.warning('Неверная скорость для Runner', exc_info=True)
        self.assertEqual(self.runner_1.distance, 50)

    def test_run(self):
        try:
            self.runner_2 = Runner(2)
            for _ in range(10):
                self.runner_2.run()
                logging.info(f'"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)
        self.assertEqual(self.runner_2.distance, 100)


if __name__ == "__main__":
    unittest.main()
