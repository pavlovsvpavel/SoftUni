from project.animals.animal import Bird


class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size: float) -> None:
        super().__init__(name, weight, wing_size)
        self.food_types = ["Meat"]

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        food_type_str = food.__class__.__name__
        if food_type_str in self.food_types:
            self.food_eaten += food.quantity
            self.weight += 0.25 * food.quantity

        return f"{__class__.__name__} does not eat {food_type_str}!"


class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size: float) -> None:
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.food_eaten += food.quantity
        self.weight += 0.35 * food.quantity



