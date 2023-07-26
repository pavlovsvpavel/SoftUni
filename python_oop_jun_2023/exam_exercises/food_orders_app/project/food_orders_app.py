from typing import List, Optional
from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    CLIENTS_PHONE_NUMBERS = []

    VALID_MEALS = {
        "Starter": Starter,
        "MainDish": MainDish,
        "Dessert": Dessert
    }

    receipt_id = 0

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    @staticmethod
    def __calculate_client_bill(client: Client):
        total_bill = 0

        for meal in client.shopping_cart:
            total_bill += meal.price * meal.quantity

        return f"{total_bill:.2f}"

    @staticmethod
    def __delete_shopping_cart_and_bill(client: Client):
        client.shopping_cart = []
        client.bill = 0

    def __meal_name_to_object(self, name):
        for meal in self.menu:
            if meal.name == name:
                return meal

        return False

    def __client_phone_number_to_object(self, phone_num):
        for client in self.clients_list:
            if client.phone_number == phone_num:
                return client

    def __validate_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def register_client(self, client_phone_number: str) -> str:
        if client_phone_number in FoodOrdersApp.CLIENTS_PHONE_NUMBERS:
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        FoodOrdersApp.CLIENTS_PHONE_NUMBERS.append(client_phone_number)
        self.clients_list.append(new_client)

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal) -> None:
        for meal in meals:
            if meal.__class__.__name__ in FoodOrdersApp.VALID_MEALS.keys():
                self.menu.append(meal)

    def show_menu(self) -> str:
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        return "\n".join(meal.details() for meal in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities) -> Optional[str]:
        self.__validate_menu()

        if client_phone_number not in FoodOrdersApp.CLIENTS_PHONE_NUMBERS:
            new_client = Client(client_phone_number)
            FoodOrdersApp.CLIENTS_PHONE_NUMBERS.append(client_phone_number)
            self.clients_list.append(new_client)

        current_client = self.__client_phone_number_to_object(client_phone_number)

        meal_in_current_order = []
        for meal, quantity in meal_names_and_quantities.items():

            current_meal = self.__meal_name_to_object(meal)
            meal_type = current_meal.__class__.__name__

            if not current_meal:
                raise Exception(f"{meal} is not on the menu!")

            if current_meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {meal_type}: {current_meal.name}!")

            meal_to_add = FoodOrdersApp.VALID_MEALS[meal_type](meal, current_meal.price, quantity)
            meal_in_current_order.append(meal_to_add)

        for c_meal in meal_in_current_order:
            for m_meal in self.menu:
                if c_meal.name == m_meal.name:
                    m_meal.quantity -= c_meal.quantity

        current_client.shopping_cart.extend(meal_in_current_order)
        current_client.bill = self.__calculate_client_bill(current_client)

        return f"Client {client_phone_number} successfully ordered " \
               f"{', '.join(m.name for m in current_client.shopping_cart)} " \
               f"for {current_client.bill}lv."

    def cancel_order(self, client_phone_number: str) -> str:
        client = next(filter(lambda x: x.phone_number == client_phone_number, self.clients_list))

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for c_meal in client.shopping_cart:
            for m_meal in self.menu:
                if c_meal.name == m_meal.name:
                    m_meal.quantity += c_meal.quantity

        self.__delete_shopping_cart_and_bill(client)

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str) -> str:
        client = next(filter(lambda x: x.phone_number == client_phone_number, self.clients_list))

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        FoodOrdersApp.receipt_id += 1
        client_bill = self.__calculate_client_bill(client)
        self.__delete_shopping_cart_and_bill(client)

        return f"Receipt #{FoodOrdersApp.receipt_id} " \
               f"with total amount of {client_bill} " \
               f"was successfully paid for {client_phone_number}."

    def __str__(self) -> str:
        return f"Food Orders App has {len(self.menu)} meals on the menu and " \
               f"{len(self.clients_list)} clients."
