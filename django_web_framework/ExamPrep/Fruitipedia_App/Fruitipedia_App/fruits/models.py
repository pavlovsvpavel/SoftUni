from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from Fruitipedia_App.profiles.models import Profile


class Fruit(models.Model):
    MIN_FRUIT_NAME_LENGTH = 2
    MAX_FRUIT_NAME_LENGTH = 25

    name = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        unique=True,
        validators=[
            MinLengthValidator(MIN_FRUIT_NAME_LENGTH),
            MaxLengthValidator(MAX_FRUIT_NAME_LENGTH)
        ],
        verbose_name="Fruit Name",

    )

    image_url = models.URLField(
        blank=False,
        null=False,
        verbose_name="Fruit Image URL",
    )

    description = models.TextField(
        blank=False,
        null=False,
        verbose_name="Fruit Description"
    )

    nutrition = models.TextField(
        blank=True,
        null=True,
        verbose_name="Nutrition Info"
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='fruits',
    )


