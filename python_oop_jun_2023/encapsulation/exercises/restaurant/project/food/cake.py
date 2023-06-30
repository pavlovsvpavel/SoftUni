from project.food.dessert import Dessert


class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name: str):
        super().__init__(name, __class__.__name__.PRICE, __class__.__name__.GRAMS, __class__.__name__.CALORIES)
