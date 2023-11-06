import re

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, RegexValidator, EmailValidator, URLValidator
from django.db import models


# def check_name(value):
#     regex = '^[a-zA-Z ]+$'
#
#     if not re.search(regex, value):
#         raise ValidationError('Name can only contain letters and spaces')


def check_phone_number(value):
    if not value.startswith('+359') or len(value) != 13:
        raise ValidationError("Phone number must start with a '+359' followed by 9 digits")


class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[RegexValidator('^[a-zA-Z ]+$', 'Name can only contain letters and spaces')]
    )

    age = models.PositiveIntegerField(
        validators=[MinValueValidator(18, 'Age must be greater than 18')]
    )

    email = models.EmailField(
        validators=[EmailValidator()]
    )

    phone_number = models.CharField(
        max_length=13,
        validators=[check_phone_number]
    )

    website_url = models.URLField(
        validators=[URLValidator()]
    )
