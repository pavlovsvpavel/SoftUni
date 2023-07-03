class Equipment:
    id = 1

    def __init__(self, name: str) -> None:
        self.name = name
        self.id = Equipment.id

    @staticmethod
    def get_next_id() -> int:
        next_id = Equipment.id
        Equipment.id += 1

        return next_id

    def __repr__(self) -> str:
        return f"Equipment <{self.id}> {self.name}"
