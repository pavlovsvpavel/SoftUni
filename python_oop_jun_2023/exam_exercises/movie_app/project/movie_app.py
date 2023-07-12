from typing import List, Optional

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self) -> None:
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def __take_username_as_object(self, username: str):
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
    def __check_for_uploaded_movie(user: User, movie_title: str) -> bool:
        for movie in user.movie_owned:
            if movie_title == movie.title:
                return True

        return False

    @staticmethod
    def __check_for_liked_movie(user: User, movie_title: str) -> bool:
        for movie in user.movie_liked:
            if movie_title == movie.title:
                return True

        return False

    def register_user(self, username: str, age: int) -> str:
        new_user = User(username, age)

        if new_user in self.users_collection:
            raise Exception("User already exists!")

        self.users_collection.append(new_user)

        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie) -> str:
        current_user = self.__check_for_registered_user(username)

        if not current_user:
            raise Exception("This user does not exist!")

        if self.__check_for_uploaded_movie(current_user, movie.title):
            raise Exception("Movie already added to the collection!")

        if not self.__check_ownership(username, movie.owner.username):
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.append(movie)
        current_user.movie_owned.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs) -> str:

        if not self.__check_ownership(username, movie.owner.username):
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if not self.__check_for_uploaded_movie(self.__take_username_as_object(username), movie.title):
            raise Exception(f"The movie {movie.title} is not uploaded!")

        for key, value in kwargs.items():
            setattr(movie, key, value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie) -> str:
        if not self.__check_ownership(username, movie.owner.username):
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if not self.__check_for_uploaded_movie(self.__take_username_as_object(username), movie.title):
            raise Exception(f"The movie {movie.title} is not uploaded!")

        self.movies_collection.remove(movie)
        self.__take_username_as_object(username).movie_owned.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie) -> str:

        if self.__check_ownership(username, movie.owner):
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if self.__check_for_liked_movie(self.__take_username_as_object(username), movie.title):
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        self.__take_username_as_object(username).movie_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie) -> str:
        if not self.__check_for_liked_movie(self.__take_username_as_object(username), movie.title):
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        self.__take_username_as_object(username).movie_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self) -> str:
        if not self.movies_collection:
            return "No movies found."

        return '\n'.join(movie.details() for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)))

    def __str__(self) -> str:
        result = []

        result.append("All users: ")
        if not self.users_collection:
            result.append("No users.")

        result.append(f"{', '.join(user.username for user in self.users_collection)}\n")

        result.append("All movies: ")
        if not self.movies_collection:
            result.append("No movies.")

        result.append(f"{', '.join(movie.title for movie in self.movies_collection)}")

        return "".join(result)
