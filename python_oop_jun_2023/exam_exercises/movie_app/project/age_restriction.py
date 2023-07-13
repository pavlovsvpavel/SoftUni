class Validation:

    @staticmethod
    def age_restriction(age: int, genre_class):
        if age < genre_class._age_restriction:
            raise ValueError(
                f"{genre_class.__class__.__name__} movies must be restricted for "
                f"audience under {genre_class._age_restriction} years!")
