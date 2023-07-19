import unittest


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class WorkerTests(unittest.TestCase):
    # def setUp(self) -> None:
    #     self.worker = Worker("Ivan", 2000, 85)

    def test_valid_initialization(self):
        worker = Worker("Ivan", 2000, 85)
        self.assertEqual("Ivan", worker.name)
        self.assertEqual(2000, worker.salary)
        self.assertEqual(85, worker.energy)

    def test_energy_increment(self):
        worker = Worker("Ivan", 2000, 85)
        worker.rest()
        self.assertEqual(86, worker.energy)

    def test_negative_or_zero_energy(self):
        worker = Worker("Gosho", 2000, 0)

        with self.assertRaises(Exception) as error:
            worker.work()
        self.assertEqual('Not enough energy.', str(error.exception))

    def test_salary_increase(self):
        worker = Worker("Ivan", 2000, 85)
        result = worker.salary
        worker.work()
        self.assertEqual(result, worker.money)

    def test_energy_decrease(self):
        worker = Worker("Ivan", 2000, 85)
        worker.work()

        self.assertEqual(84, worker.energy)

    def test_get_info(self):
        worker = Worker("Ivan", 2000, 85)
        worker.work()
        result = worker.get_info()
        expected_result = "Ivan has saved 2000 money."

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
