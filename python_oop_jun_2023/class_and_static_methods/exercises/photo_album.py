from typing import List
from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.photos: List = self.__album_creation()

    def __album_creation(self):
        matrix = [[] for _ in range(self.pages)]

        return matrix

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE))

    def add_photo(self, label: str) -> str:
        for page_num, row in enumerate(self.photos, 1):
            if len(row) < PhotoAlbum.PHOTOS_PER_PAGE:
                row.append(label)

                return f"{label} photo added successfully on page " \
                       f"{page_num} slot {row.index(label) + 1}"

        return "No more free slots"

    def display(self) -> str:
        result = ["-----------"]

        for row in self.photos:

            if len(row) == 0:
                result.append("\n-----------\n")
                continue

            row_photos = ["[]" for _ in row]

            result.append(" ".join(row_photos))

            result.append("-----------")

        return "\n".join(result)


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())
