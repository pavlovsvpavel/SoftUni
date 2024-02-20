from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from Music_App.profiles.validators import validate_username


class Profile(models.Model):
    MAX_USERNAME_LENGTH = 15
    MIN_USERNAME_LENGTH = 2

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=[
            MinLengthValidator(MIN_USERNAME_LENGTH),
            MaxLengthValidator(MAX_USERNAME_LENGTH),
            validate_username,
        ],
        verbose_name="Username",
    )
    email = models.EmailField(
        blank=False,
        null=False,
        verbose_name="Email"
    )

    age = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        verbose_name="Age"
    )

