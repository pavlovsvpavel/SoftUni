from abc import abstractmethod, ABC


class Food(ABC):
    def __init__(self, quantity: int) -> None:
        self.quantity = quantity

    @abstractmethod
    def feed(self, food):
        pass


class Vegetable(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)

    def feed(self, food):
        return food


class Fruit(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)

    def feed(self, food):
        return food


class Meat(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)

    def feed(self, food):
        return food


class Seed(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)

    def feed(self, food):
        return food
