from django.core.exceptions import ValidationError


def validate_name(value):
    if not value.strip()[0].isalpha():
        raise ValidationError("Your name must start with a letter!")

