from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    def __init__(self):
        super().__init__(interest_rate=1.5, amount=2_000.0)

    def increase_interest_rate(self) -> None:
        self.interest_rate += 0.2
