from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from django.db import models
from World_Of_Speed_App.profiles.validators import validate_username


class Profile(models.Model):
    MAX_USERNAME_LENGTH = 15
    MIN_USERNAME_LENGTH = 3
    MIN_AGE = 21
    MAX_PASSWORD_LENGTH = 20
    MAX_NAME_LENGTH = 25

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name

        return False

    username = models.CharField(
        max_length=15,
        blank=False,
        null=False,
        validators=(
            MinLengthValidator(MIN_USERNAME_LENGTH, "Username must be at least 3 chars long!"),
            MaxLengthValidator(MAX_USERNAME_LENGTH),
            validate_username,
        )
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.IntegerField(
        blank=False,
        null=False,
        validators=(
            MinValueValidator(MIN_AGE),
        )
    )

    password = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        validators=(
            MaxLengthValidator(MAX_PASSWORD_LENGTH),
        )
    )

    first_name = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        validators=(
            MaxLengthValidator(MAX_NAME_LENGTH),
        )
    )

    last_name = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        validators=(
            MaxLengthValidator(MAX_NAME_LENGTH),
        )
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )


