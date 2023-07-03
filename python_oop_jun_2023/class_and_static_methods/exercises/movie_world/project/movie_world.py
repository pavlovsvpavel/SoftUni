from typing import List

from project.customer import Customer

from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str) -> None:
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity() -> int:
        return 15

    @staticmethod
    def customer_capacity() -> int:
        return 10

    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        try:
            c_customer = next(filter(lambda x: x.id == customer_id, self.customers))
        except StopIteration:
            return "Invalid customer id"

        try:
            c_dvd = next(filter(lambda x: x.id == dvd_id, self.dvds))
        except StopIteration:
            return "Invalid dvd id"

        if c_dvd in c_customer.rented_dvds:
            return f"{c_customer.name} has already rented {c_dvd.name}"

        if not c_dvd.is_rented:
            if c_dvd.age_restriction <= c_customer.age:
                c_dvd.is_rented = True
                c_customer.rented_dvds.append(c_dvd)
                return f"{c_customer.name} has successfully rented {c_dvd.name}"

            return f"{c_customer.name} should be at least {c_dvd.age_restriction} to rent this movie"

        return "DVD is already rented"

    def return_dvd(self, customer_id: int, dvd_id: int) -> str:
        try:
            c_customer = next(filter(lambda x: x.id == customer_id, self.customers))
        except StopIteration:
            return "Invalid customer id"

        try:
            c_dvd = next(filter(lambda x: x.id == dvd_id, self.dvds))
        except StopIteration:
            return "Invalid dvd id"

        if c_dvd in c_customer.rented_dvds:
            c_dvd.is_rented = False
            c_customer.rented_dvds.remove(c_dvd)

            return f"{c_customer.name} has successfully returned {c_dvd.name}"

        return f"{c_customer.name} does not have that DVD"

    def __repr__(self) -> str:
        result = []

        for cust in self.customers:
            result.append(str(cust))

        for dvd in self.dvds:
            result.append(str(dvd))

        return "\n".join(result)
