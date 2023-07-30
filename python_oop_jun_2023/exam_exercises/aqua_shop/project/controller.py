from typing import List, Optional
from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    VALID_AQUARIUM_TYPES = {
        "FreshwaterAquarium": FreshwaterAquarium,
        "SaltwaterAquarium": SaltwaterAquarium
    }

    VALID_DECORATION = {
        "Ornament": Ornament,
        "Plant": Plant
    }

    VALID_FISH_TYPES = {
        "FreshwaterFish": FreshwaterFish,
        "SaltwaterFish": SaltwaterFish
    }

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums: List[BaseAquarium] = []

    def __find_aquarium_by_name(self, name):
        for aquarium in self.aquariums:
            if aquarium.name == name:
                return aquarium

    def __find_fish_by_name(self, name):
        for aquarium in self.aquariums:
            for fish in aquarium.fish:
                if fish.name == name:
                    return fish

    def add_aquarium(self, aquarium_type: str, aquarium_name: str) -> str:
        if aquarium_type not in Controller.VALID_AQUARIUM_TYPES:
            return "Invalid aquarium type."

        new_aquarium = Controller.VALID_AQUARIUM_TYPES[aquarium_type](aquarium_name)

        self.aquariums.append(new_aquarium)

        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str) -> str:
        if decoration_type not in Controller.VALID_DECORATION:
            return "Invalid decoration type."

        new_decoration = Controller.VALID_DECORATION[decoration_type]()

        self.decorations_repository.add(new_decoration)

        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str) -> Optional[str]:
        current_decoration = self.decorations_repository.find_by_type(decoration_type)

        if not current_decoration:
            return f"There isn't a decoration of type {decoration_type}."

        current_aquarium = self.__find_aquarium_by_name(aquarium_name)

        if not current_aquarium:
            return

        current_aquarium.add_decoration(current_decoration)
        self.decorations_repository.remove(current_decoration)

        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str,
                 fish_species: str, price: float) -> Optional[str]:

        if fish_type not in Controller.VALID_FISH_TYPES:
            return f"There isn't a fish of type {fish_type}."

        current_aquarium = self.__find_aquarium_by_name(aquarium_name)

        if not current_aquarium:
            return

        if fish_type[:-4] not in current_aquarium.__class__.__name__:
            return "Water not suitable."

        new_fish = Controller.VALID_FISH_TYPES[fish_type](fish_name, fish_species, price)
        return current_aquarium.add_fish(new_fish)

    def feed_fish(self, aquarium_name: str) -> Optional[str]:
        current_aquarium = self.__find_aquarium_by_name(aquarium_name)

        if not current_aquarium:
            return

        current_aquarium.feed()

        return f"Fish fed: {len(current_aquarium.fish)}"

    def calculate_value(self, aquarium_name: str) -> Optional[str]:
        current_aquarium = self.__find_aquarium_by_name(aquarium_name)

        if not current_aquarium:
            return

        total_value = 0
        for obj in [current_aquarium.fish, current_aquarium.decorations]:
            for attr in obj:
                if attr == "None":
                    continue

                total_value += attr.price

        return f"The value of Aquarium {aquarium_name} is {total_value:.2f}."

    def report(self) -> str:
        result = []

        for aquarium in self.aquariums:
            result.append(aquarium.__str__())

        return "\n".join(result)
