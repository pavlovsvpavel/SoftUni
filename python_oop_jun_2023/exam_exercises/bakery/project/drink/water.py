from project.drink.drink import Drink


class Water(Drink):
    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, 1.50, brand)

    def __repr__(self) -> str:
        return (f" - {self.name} {self.brand} - {self.portion:.2f}ml "
                f"- {self.price:.2f}lv"
                )
