from project.movie_specification.movie import Movie
from project.user import User


class Action(Movie):
    _age_restriction = 12

    def __init__(self, title: str, year: int, owner: User, age_restriction: int = 12) -> None:
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < 12:
            raise ValueError("Action movies must be restricted for audience under 12 years!")

        self.__age_restriction = value

    def details(self) -> str:
        return f"Action - Title:{self.title}, " \
               f"Year:{self.year}, " \
               f"Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, " \
               f"Owned by:{self.owner.username}"
