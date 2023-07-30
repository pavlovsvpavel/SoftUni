from typing import List, Optional

from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class Bakery:
    VALID_FOOD_TYPES = {
        "Bread": Bread,
        "Cake": Cake
    }

    VALID_DRINK_TYPES = {
        "Tea": Tea,
        "Water": Water
    }

    VALID_TABLES_TYPES = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable
    }

    def __init__(self, name: str):
        self.name = name
        self.food_menu: List[BakedFood] = []
        self.drinks_menu: List[Drink] = []
        self.tables_repository: List[Table] = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")

        self.__name = value

    def add_food(self, food_type: str, name: str, price: float) -> Optional[str]:
        try:
            new_food = Bakery.VALID_FOOD_TYPES[food_type](name, price)
        except KeyError:
            return

        for food in self.food_menu:
            if food.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")

        self.food_menu.append(new_food)

        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str) -> Optional[str]:
        try:
            new_drink = Bakery.VALID_DRINK_TYPES[drink_type](name, portion, brand)
        except KeyError:
            return

        for drink in self.drinks_menu:
            if drink.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")

        self.drinks_menu.append(new_drink)

        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int) -> Optional[str]:
        try:
            new_table = Bakery.VALID_TABLES_TYPES[table_type](table_number, capacity)
        except KeyError:
            return

        for table in self.tables_repository:
            if table.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        self.tables_repository.append(new_table)

        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int) -> str:
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)

                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        else:
            return f"No available table for {number_of_people} people"

    def __find_table_number_as_object(self, number):
        for table in self.tables_repository:
            if table.table_number == number:
                return table

    def __find_food_name_as_object(self, name):
        for food in self.food_menu:
            if food.name == name:
                return food

    def __find_drink_name_as_object(self, name):
        for drink in self.drinks_menu:
            if drink.name == name:
                return drink

    def order_food(self, table_number: int, *food_names: str) -> str:
        current_table = self.__find_table_number_as_object(table_number)

        if not isinstance(current_table, Table):
            return f"Could not find table {table_number}"

        foods_not_in_menu = []

        for food_name in food_names:
            current_food = self.__find_food_name_as_object(food_name)

            if current_food and current_food in self.food_menu:
                current_table.order_food(current_food)
            else:
                foods_not_in_menu.append(food_name)

        result = [f"Table {current_table.table_number} ordered:\n"
                  f"{chr(10).join(ordered.__repr__() for ordered in current_table.food_orders)}",
                  f"{self.name} does not have in the menu:\n"
                  f"{chr(10).join(foods_not_in_menu)}"]

        return "\n".join(result)

    def order_drink(self, table_number: int, *drinks_names: str):
        current_table = self.__find_table_number_as_object(table_number)

        if not isinstance(current_table, Table):
            return f"Could not find table {table_number}"

        drinks_not_in_menu = []

        for drink_name in drinks_names:
            current_drink = self.__find_drink_name_as_object(drink_name)

            if current_drink and current_drink in self.drinks_menu:
                current_table.order_drink(current_drink)
            else:
                drinks_not_in_menu.append(drink_name)

        result = [f"Table {current_table.table_number} ordered:\n"
                  f"{chr(10).join(ordered.__repr__() for ordered in current_table.drink_orders)}",
                  f"{self.name} does not have in the menu:\n"
                  f"{chr(10).join(drinks_not_in_menu)}"]

        return "\n".join(result)

    def leave_table(self, table_number: int) -> str:
        current_table = self.__find_table_number_as_object(table_number)

        table_bill = current_table.get_bill()
        current_table.clear()
        current_table.is_reserved = not current_table.is_reserved
        self.total_income += table_bill

        return f"Table: {table_number}\n" \
               f"Bill: {table_bill:.2f}"

    def get_free_tables_info(self) -> str:
        result = []

        for table in self.tables_repository:
            result.append(table.free_table_info())

        return "\n".join(result)

    def get_total_income(self) -> str:
        return f"Total income: {self.total_income:.2f}lv"
