from typing import List, Optional
from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOANS_TYPES = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan
    }

    VALID_CLIENT_TYPES = {
        "Student": Student,
        "Adult": Adult
    }

    VALID_GRANT_LOANS = {
        "Student": "StudentLoan",
        "Adult": "MortgageLoan"
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def __find_client_by_client_id(self, client_id):
        for client in self.clients:
            if client.client_id == client_id:
                return client

    def __find_loan_by_name(self, loan_type):
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                return loan

    def add_loan(self, loan_type: str) -> str:
        if loan_type not in BankApp.VALID_LOANS_TYPES.keys():
            raise Exception("Invalid loan type!")

        new_loan = BankApp.VALID_LOANS_TYPES[loan_type]()

        self.loans.append(new_loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float) -> str:
        if client_type not in BankApp.VALID_CLIENT_TYPES.keys():
            raise Exception("Invalid client type!")

        if len(self.clients) == self.capacity:
            return "Not enough bank capacity."

        new_client = BankApp.VALID_CLIENT_TYPES[client_type](client_name, client_id, income)

        self.clients.append(new_client)

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str) -> Optional[str]:
        current_client = self.__find_client_by_client_id(client_id)

        client_type = current_client.__class__.__name__

        if client_type not in BankApp.VALID_GRANT_LOANS or loan_type != BankApp.VALID_GRANT_LOANS[client_type]:
            raise Exception("Inappropriate loan type!")

        try:
            current_loan = [loan for loan in self.loans if loan.__class__.__name__ == loan_type][0]
        except IndexError:
            return

        self.loans.remove(current_loan)
        current_client.loans.append(current_loan)

        return f"Successfully granted {loan_type} to {current_client.name} with ID {client_id}."

    def remove_client(self, client_id: str) -> str:
        try:
            current_client = next(filter(lambda x: x.client_id == client_id, self.clients))
        except StopIteration:
            raise Exception("No such client!")

        if current_client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(current_client)

        return f"Successfully removed {current_client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str) -> str:
        number_of_changed_loans = 0

        for loan in self.loans:
            c_loan_type = loan.__class__.__name__
            if c_loan_type in BankApp.VALID_LOANS_TYPES.keys() and c_loan_type == loan_type:
                loan.increase_interest_rate()
                number_of_changed_loans += 1

        return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate: float) -> str:
        changed_client_rates_number = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_client_rates_number += 1

        return f"Number of clients affected: {changed_client_rates_number}."

    def get_statistics(self) -> str:
        total_sum_granted_loans = 0

        for c in self.clients:
            if c.loans:
                for loan in c.loans:
                    total_sum_granted_loans += loan.amount

        try:
            avg_client_interest_rate = sum([c.interest for c in self.clients]) / len(self.clients)
        except ZeroDivisionError:
            avg_client_interest_rate = 0

        result = [f"Active Clients: {len(self.clients)}",
                  f"Total Income: {sum([c.income for c in self.clients]):.2f}",
                  f"Granted Loans: {sum([len(c.loans) for c in self.clients if c.loans])}, "
                  f"Total Sum: {total_sum_granted_loans:.2f}",
                  f"Available Loans: {len(self.loans)}, "
                  f"Total Sum: {sum([l.amount for l in self.loans]):.2f}",
                  f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"]

        return "\n".join(result)
