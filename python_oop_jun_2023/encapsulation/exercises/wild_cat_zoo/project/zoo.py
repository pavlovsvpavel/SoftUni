from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price

            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if self.__budget < price and self.__animal_capacity > len(self.animals):
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"

        self.workers.append(worker)

        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        try:
            c_name = next(filter(lambda x: x.name == worker_name, self.workers))

        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(c_name)
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        total_salaries = sum(worker.salary for worker in self.workers)

        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total_money_for_tend = sum(animal.money_for_care for animal in self.animals)

        if self.__budget >= total_money_for_tend:
            self.__budget -= total_money_for_tend
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        all_animals = {"Lion": [], "Tiger": [], "Cheetah": []}

        for c_animal in self.animals:
            all_animals[c_animal.__class__.__name__].append(str(c_animal))

        result = [f"You have {len(self.animals)} animals",
                  f"----- {len(all_animals['Lion'])} Lions:", *all_animals['Lion'],
                  f"----- {len(all_animals['Tiger'])} Tigers:", *all_animals['Tiger'],
                  f"----- {len(all_animals['Cheetah'])} Cheetahs:", *all_animals['Cheetah']]

        return "\n".join(result)

    def workers_status(self) -> str:
        all_workers = {"Keeper": [], "Caretaker": [], "Vet": []}

        for c_worker in self.workers:
            all_workers[c_worker.__class__.__name__].append(str(c_worker))

        result = [f"You have {len(self.workers)} workers",
                  f"----- {len(all_workers['Keeper'])} Keepers:", *all_workers['Keeper'],
                  f"----- {len(all_workers['Caretaker'])} Caretakers:", *all_workers['Caretaker'],
                  f"----- {len(all_workers['Vet'])} Vets:", *all_workers['Vet']]

        return "\n".join(result)
