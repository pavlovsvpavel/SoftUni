class Room:
    def __init__(self, number: int, capacity: int) -> None:
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people: int) -> None or str:

        if self.capacity >= self.guests + people and not self.is_taken:
            self.guests += people
            self.is_taken = True

        return f"Room number {self.number} cannot be taken"

    def free_room(self) -> None or str:
        if self.is_taken:
            self.is_taken = False
            self.guests = 0

        return f"Room number {self.number} is not taken"

