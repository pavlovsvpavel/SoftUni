from project.movie_specification.movie import Movie
from project.user import User


class Fantasy(Movie):
    _age_restriction = 6

    def __init__(self, title: str, year: int, owner: User, age_restriction: int = 6) -> None:
        super().__init__(title, year, owner, age_restriction)

    def details(self) -> str:
        return f"Fantasy - Title:{self.title}, " \
               f"Year:{self.year}, " \
               f"Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, " \
               f"Owned by:{self.owner.username}"
