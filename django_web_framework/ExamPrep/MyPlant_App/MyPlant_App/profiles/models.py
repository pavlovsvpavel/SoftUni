from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from MyPlant_App.profiles.validators import validate_profile_name


class Profile(models.Model):
    MIN_USERNAME_LENGTH = 2
    MAX_USERNAME_LENGTH = 10
    MAX_FIRST_LAST_NAME_LENGTH = 20

    username = models.CharField(
        max_length=10,
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(MIN_USERNAME_LENGTH),
            MaxLengthValidator(MAX_USERNAME_LENGTH)
        ],

    )

    first_name = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        validators=[
            MaxLengthValidator(MAX_FIRST_LAST_NAME_LENGTH),
            validate_profile_name
        ],
        verbose_name="First Name",
    )

    last_name = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        validators=[
            MaxLengthValidator(MAX_FIRST_LAST_NAME_LENGTH),
            validate_profile_name
        ],
        verbose_name="Last Name",
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
        verbose_name="Profile Picture",
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



