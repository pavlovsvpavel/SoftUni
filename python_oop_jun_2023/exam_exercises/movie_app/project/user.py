from typing import List


class User:
    def __init__(self, username: str, age: int) -> None:
        self.username = username
        self.age = age
        self.movies_liked: List[object] = []
        self.movies_owned: List[object] = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value == "":
            raise ValueError("Invalid username!")

        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")

        self.__age = value

    def __str__(self) -> str:
        result = [f"Username: {self.username}, Age: {self.age}"]

        if self.movies_liked:
            result.append(f"Liked movies:\n{chr(10).join(m.details() for m in self.movies_liked)}")
        else:
            result.append("No movies liked.")

        if self.movies_owned:
            result.append(f"Owned movies:\n{chr(10).join(m.details() for m in self.movies_owned)}")
        else:
            result.append("No movies owned.")

        return "\n".join(result)
