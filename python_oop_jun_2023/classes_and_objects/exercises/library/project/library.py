from typing import List, Dict

from project.user import User


class Library:
    def __init__(self):
        self.user_records: List[User] = []  # [Object_1, Object_2 ...]
        self.books_available: Dict[str:[str]] = {}  # {Author: [Book_1, Book_2...]
        self.rented_books: Dict[str:{str: int}] = {}  # {Username: {Book_1: 10,  Book_2: 20...}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        if book_name in self.books_available[author]:
            user.books.append(book_name)

            if user.username in self.rented_books:
                self.rented_books[user.username][book_name] = days_to_return
            else:
                self.rented_books[user.username] = {book_name: days_to_return}

            idx = self.books_available[author].index(book_name)
            del self.books_available[author][idx]

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        return f'The book "{book_name}" is already rented and will be available in ' \
               f'{self.rented_books[user.username][book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User) -> str:
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            del self.rented_books[user.username][book_name]

        return f"{user.username} doesn't have this book in his/her records!"
