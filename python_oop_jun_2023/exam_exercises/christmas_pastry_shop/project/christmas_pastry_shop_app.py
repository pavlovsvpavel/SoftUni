from typing import List
from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACIES = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen
    }

    VALID_BOOTH_TYPES = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth
    }

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float) -> str:
        for delicacy in self.delicacies:
            if delicacy.name == name:
                raise Exception(f"{name} already exists!")

        if type_delicacy not in ChristmasPastryShopApp.VALID_DELICACIES.keys():
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        new_delicacy = ChristmasPastryShopApp.VALID_DELICACIES[type_delicacy](name, price)

        self.delicacies.append(new_delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int) -> str:
        for booth in self.booths:
            if booth.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in ChristmasPastryShopApp.VALID_BOOTH_TYPES.keys():
            raise Exception(f"{type_booth} is not a valid booth!")

        new_booth = ChristmasPastryShopApp.VALID_BOOTH_TYPES[type_booth](booth_number, capacity)

        self.booths.append(new_booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int) -> str:
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)

                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str) -> str:
        try:
            current_booth = next(filter(lambda x: x.booth_number == booth_number, self.booths))
        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            current_delicacy = next(filter(lambda x: x.name == delicacy_name, self.delicacies))
        except StopIteration:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        current_booth.delicacy_orders.append(current_delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int) -> str:
        current_booth = next(filter(lambda x: x.booth_number == booth_number, self.booths))

        booth_bill = current_booth.price_for_reservation + sum([d.price for d in current_booth.delicacy_orders])

        self.income += booth_bill

        current_booth.delicacy_orders = []
        current_booth.is_reserved = not current_booth.is_reserved
        current_booth.price_for_reservation = 0

        return f"Booth {booth_number}:\n" \
               f"Bill: {booth_bill:.2f}lv."

    def get_income(self) -> str:
        return f"Income: {self.income:.2f}lv."
