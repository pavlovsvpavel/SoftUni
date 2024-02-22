from django.core.exceptions import ValidationError


def validate_fruit_name(value):
    if not any(ch.isalpha() for ch in value):
        raise ValidationError("Fruit name should contain only letters!")
