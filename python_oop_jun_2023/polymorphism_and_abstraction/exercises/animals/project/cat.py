from project.animal import Animal


class Cat(Animal):
    def __init__(self, name: str, age: int, gender: str) -> None:
        super().__init__(name, age, gender)

    def make_sound(self) -> str:
        return "Meow meow!"
