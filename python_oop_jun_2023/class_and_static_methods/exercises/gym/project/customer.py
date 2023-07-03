class Customer:
    id = 1

    def __init__(self, name: str, address: str, email: str) -> None:
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.id

    @staticmethod
    def get_next_id() -> int:
        next_id = Customer.id
        Customer.id += 1

        return next_id

    def __repr__(self) -> str:
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
