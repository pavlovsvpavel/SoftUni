from django.core.exceptions import ValidationError


def validate_username(username):
    if not all(char.isalnum() or char == "_" for char in username):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
