from abc import ABC, abstractmethod
from math import log2


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    @abstractmethod
    def computer_type(self):
        pass

    @property
    @abstractmethod
    def processor_models(self):
        pass

    @property
    @abstractmethod
    def max_ram(self):
        pass

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == "":
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == "":
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    @staticmethod
    def power_of_two(ram: int):
        result = log2(ram)
        return result.is_integer()

    def configure_computer(self, processor: str, ram: int) -> str:
        if not self.processor_models.get(processor):
            raise ValueError(f"{processor} is not compatible with {self.computer_type} {self.manufacturer} {self.model}!")

        if not self.power_of_two(ram) or ram > self.max_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with {self.computer_type} {self.manufacturer} {self.model}!")

        self.set_parts(processor, ram)

        return f"Created {self.__repr__()} for {self.price}$."

    def set_parts(self, processor: str, ram: int) -> None:
        self.processor = processor
        self.ram = ram
        self.price += self.processor_models[processor]
        self.price += int(log2(ram)) * 100

    def __repr__(self) -> str:
        return f"{self.__manufacturer} {self.__model} with {self.processor} and {self.ram}GB RAM"
