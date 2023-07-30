from abc import ABC, abstractmethod
from typing import List
from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders: List[BakedFood] = []
        self.drink_orders: List[Drink] = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")

        self.__capacity = value

    def reserve(self, number_of_people: int) -> None:
        self.is_reserved = not self.is_reserved
        self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood) -> None:
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink) -> None:
        self.drink_orders.append(drink)

    def get_bill(self) -> float:
        total_bill = 0

        for obj in [self.food_orders, self.drink_orders]:
            for attr in obj:
                total_bill += attr.price

        return total_bill

    def clear(self) -> None:
        self.food_orders, self.drink_orders = [], []
        self.number_of_people = 0

    def free_table_info(self) -> str:
        if not self.is_reserved:
            return f"Table: {self.table_number}\n"\
                   f"Type: {self.__class__.__name__}\n"\
                   f"Capacity: {self.capacity}"
