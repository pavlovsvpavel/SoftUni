from typing import List

from project.dvd import DVD


class Customer:
    def __init__(self, name: str, age: int, id_num: int) -> None:
        self.name = name
        self.age = age
        self.id = id_num
        self.rented_dvds: List[DVD] = []

    def __repr__(self) -> str:
        all_rented_dvd_names = []

        for rented_dvd in self.rented_dvds:
            all_rented_dvd_names.append(rented_dvd.name)

        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} " \
               f"rented DVD's ({', '.join(all_rented_dvd_names)})"
