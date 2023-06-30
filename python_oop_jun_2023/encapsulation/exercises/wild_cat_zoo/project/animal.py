class Animal:
    def __init__(self, name: str, gender: str, age: int, money: int):
        self.name = name
        self.gender = gender
        self.age = age
        self.money_for_care = money

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

