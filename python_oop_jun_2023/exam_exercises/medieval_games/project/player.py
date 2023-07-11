from typing import List


class Player:
    players_names: List[str] = []

    def __init__(self, name: str, age: int, stamina: int = 100) -> None:
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")

        elif value in Player.players_names:
            raise Exception(f"Name {value} is already used!")

        self.__name = value
        Player.players_names.append(value)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")

        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < 0 or value > 100:
            raise ValueError("Stamina not valid!")

        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.stamina < 100

    def __str__(self) -> str:
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
