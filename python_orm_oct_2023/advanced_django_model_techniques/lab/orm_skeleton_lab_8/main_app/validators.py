from django.core.exceptions import ValidationError


def validate_menu_categories(value):
    categories = ["Appetizers", "Main Course", "Desserts"]

    matches = 0
    for el in categories:
        if value.lower().find(el.lower()) > 0:
            matches += 1

    if matches < len(categories):
        raise ValidationError(
            'The menu must include each of the categories "Appetizers", "Main Course", "Desserts".'
        )
