from typing import List, Optional

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self) -> None:
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def __username_as_object(self, username: str):
        for user in self.users_collection:
            if user.username == username:
                return user

    def __check_for_registered_user(self, username: str) -> Optional[User]:
        try:
            valid_user = next(filter(lambda x: x.username == username, self.users_collection))
        except StopIteration:
            return

        return valid_user

    @staticmethod
    def __check_ownership(username: str, movie_owner: str) -> bool:
        return username == movie_owner

    @staticmethod
    def __check_for_uploaded_movie(movie: Movie, uploaded_movies) -> bool:
        if movie in uploaded_movies:
            return True

        return False

    @staticmethod
    def __check_for_liked_movie(movie: Movie, liked_movies) -> bool:
        if movie in liked_movies:
            return True

        return False

    def register_user(self, username: str, age: int) -> str:
        new_user = User(username, age)

        for user in self.users_collection:
            if user.username == username:
                raise Exception("User already exists!")

        self.users_collection.append(new_user)

        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie) -> str:
        current_user = self.__check_for_registered_user(username)

        if not current_user:
            raise Exception("This user does not exist!")

        if not self.__check_ownership(username, movie.owner.username):
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if self.__check_for_uploaded_movie(movie, self.movies_collection):
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        current_user.movies_owned.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs) -> str:
        if not self.__check_for_uploaded_movie(movie, self.movies_collection):
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if not self.__check_ownership(username, movie.owner.username):
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            setattr(movie, key, value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie) -> str:
        if not self.__check_for_uploaded_movie(movie, self.movies_collection):
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if not self.__check_ownership(username, movie.owner.username):
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        self.__username_as_object(username).movies_owned.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie) -> str:

        if self.__check_ownership(username, movie.owner.username):
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if self.__check_for_liked_movie(movie, self.__username_as_object(username).movies_liked):
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        self.__username_as_object(username).movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie) -> str:
        if not self.__check_for_liked_movie(movie, self.__username_as_object(username).movies_liked):
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        self.__username_as_object(username).movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self) -> str:
        if not self.movies_collection:
            return "No movies found."

        return '\n'.join(movie.details() for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)))

    def __str__(self) -> str:
        result = ["All users: "]

        if not self.users_collection:
            result[0] += "No users."
        else:
            result[0] += ', '.join(u.username for u in self.users_collection)

        result.append("All movies: ")

        if not self.movies_collection:
            result[1] += "No movies."
        else:
            result[1] += ', '.join(u.title for u in self.movies_collection)

        return "\n".join(result)
