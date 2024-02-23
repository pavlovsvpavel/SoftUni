from django.core.exceptions import ValidationError


def validate_plant_name(value):
    if not all(ch.isalpha() for ch in value):
        raise ValidationError("Plant name should contain only letters!")
