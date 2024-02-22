from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from Fruitipedia_App.profiles.validators import validate_name


class Profile(models.Model):
    MIN_FIRST_NAME_LENGTH = 2
    MAX_FIRST_NAME_LENGTH = 25
    MIN_LAST_NAME_LENGTH = 1
    MAX_LAST_NAME_LENGTH = 35
    MAX_EMAIL_LENGTH = 40
    MIN_PASSWORD_LENGTH = 8
    MAX_PASSWORD_LENGTH = 20

    first_name = models.CharField(
        max_length=25,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(MIN_FIRST_NAME_LENGTH),
            MaxLengthValidator(MAX_FIRST_NAME_LENGTH),
            validate_name,
        ],
        verbose_name="First Name",
    )

    last_name = models.CharField(
        max_length=35,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(MIN_LAST_NAME_LENGTH),
            MaxLengthValidator(MAX_LAST_NAME_LENGTH),
            validate_name
        ],
        verbose_name="Last Name",
    )

    email = models.EmailField(
        max_length=40,
        blank=False,
        null=False,
        unique=True,
        validators=[
            MaxLengthValidator(MAX_EMAIL_LENGTH)
        ],
        verbose_name="Email",
    )

    password = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(MIN_PASSWORD_LENGTH),
            MaxLengthValidator(MAX_PASSWORD_LENGTH)
        ],
        verbose_name="Password",
    )

    image_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Image URL",
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=18,
        verbose_name="Age",
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
