from abc import ABC, abstractmethod
from typing import List
from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class BaseAquarium(ABC):
    VALID_FISH_TYPES = {
        "FreshwaterFish": FreshwaterFish,
        "SaltwaterFish": SaltwaterFish
    }

    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations: List[BaseDecoration] = []
        self.fish: List[BaseFish] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")

        self.__name = value

    def calculate_comfort(self) -> int:
        comfort = 0

        for decoration in self.decorations:
            if decoration == "None":
                continue

            comfort += decoration.comfort

        return comfort

    def add_fish(self, fish: BaseFish) -> str:
        if len(self.fish) == self.capacity:
            return "Not enough capacity."

        fish_type = fish.__class__.__name__
        if fish_type in BaseAquarium.VALID_FISH_TYPES:
            self.fish.append(fish)

            return f"Successfully added {fish_type} to {self.name}."

    def remove_fish(self, fish: BaseFish) -> None:
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration) -> None:
        self.decorations.append(decoration)

    def feed(self) -> None:
        for fish in self.fish:
            fish.eat()

    def __str__(self) -> str:
        result = [f"{self.name}:"]

        if self.fish:
            result.append(f"Fish: {' '.join(f.name for f in self.fish)}")
        else:
            result.append("Fish: none")

        result.append(f"Decorations: {len(self.decorations)}")

        result.append(f"Comfort: {self.calculate_comfort()}")

        return "\n".join(result)

