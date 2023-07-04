from calendar import month_name


class DVD:
    def __init__(self, name: str, id_num: int, creation_year: int, creation_month: str, age_restriction: int) -> None:
        self.name = name
        self.id = id_num
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id_num: int, name: str, date: str, age_restriction: int):
        date_elements = date.split(".")
        day, month, year = date_elements[0], int(date_elements[1]), int(date_elements[2])

        return cls(name, id_num, year, month_name[month], age_restriction)

    def __repr__(self) -> str:
        status = "rented" if self.is_rented else "not rented"

        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {status}"
