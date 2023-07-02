from typing import List

from project.room import Room


class Hotel:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number, people) -> None:
        try:
            c_room_number = next(filter(lambda x: x.number == room_number, self.rooms))
            if c_room_number.guests + people <= c_room_number.capacity and not c_room_number.is_taken:
                self.guests += people
                c_room_number.guests += people
                c_room_number.is_taken = True

        except StopIteration:
            pass

    def free_room(self, room_number: int) -> None:
        try:
            c_room_number = next(filter(lambda x: x.number == room_number, self.rooms))
            if c_room_number.is_taken:
                c_room_number.is_taken = False
                self.guests -= c_room_number.guests
                c_room_number.guests -= c_room_number.guests

        except StopIteration:
            pass

    def status(self) -> str:
        result = [f"Hotel {self.name} has {self.guests} total guests",
                  f"Free rooms: {', '.join(map(str, (room.number for room in self.rooms if not room.is_taken)))}",
                  f"Taken rooms: {', '.join(map(str, (room.number for room in self.rooms if room.is_taken)))}"
                  ]

        return "\n".join(result)
