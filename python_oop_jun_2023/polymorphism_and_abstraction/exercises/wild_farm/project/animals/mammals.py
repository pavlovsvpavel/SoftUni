from project.animals.animal import Mammal


class Mouse(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.food_types = ["Vegetable", "Fruit"]

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        food_type_str = food.__class__.__name__
        if food_type_str in self.food_types:
            self.food_eaten += food.quantity
            self.weight += 0.10 * food.quantity

        return f"{__class__.__name__} does not eat {food_type_str}!"


class Dog(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.food_types = ["Meat"]

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        food_type_str = food.__class__.__name__
        if food_type_str in self.food_types:
            self.food_eaten += food.quantity
            self.weight += 0.40 * food.quantity

        return f"{__class__.__name__} does not eat {food_type_str}!"


class Cat(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.food_types = ["Vegetable", "Meat"]

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        food_type_str = food.__class__.__name__
        if food_type_str in self.food_types:
            self.food_eaten += food.quantity
            self.weight += 0.30 * food.quantity

        return f"{__class__.__name__} does not eat {food_type_str}!"


class Tiger(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.food_types = ["Meat"]

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        food_type_str = food.__class__.__name__
        if food_type_str in self.food_types:
            self.food_eaten += food.quantity
            self.weight += food.quantity

        return f"{__class__.__name__} does not eat {food_type_str}!"
