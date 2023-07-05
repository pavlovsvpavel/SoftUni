from project.animal import Animal


class Dog(Animal):
    def __init__(self, name: str, age: int, gender: str) -> None:
        super().__init__(name, age, gender)

    def make_sound(self) -> str:
        return "Woof!"
