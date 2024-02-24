from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from World_Of_Speed_App.cars.validators import validate_car_year
from World_Of_Speed_App.profiles.models import Profile


class Car(models.Model):
    MIN_LENGTH_MODEL_NAME = 1
    MAX_LENGTH_MODEL_NAME = 15
    MIN_CAR_PRICE = 1.0

    class CarTypeChoices(models.TextChoices):
        RALLY = "Rally", _("Rally")
        OPEN_WHEEL = "Open-wheel", _("Open-wheel")
        KART = "Kart", _("Kart")
        DRAG = "Drag", _("Drag")
        OTHER = "Other", _("Other")

    type = models.CharField(
        max_length=10,
        blank=False,
        null=False,
        choices=CarTypeChoices.choices,
    )

    model = models.CharField(
        max_length=15,
        blank=False,
        null=False,
        validators=(
            MinLengthValidator(MIN_LENGTH_MODEL_NAME),
            MaxLengthValidator(MAX_LENGTH_MODEL_NAME),
        ),
    )

    year = models.IntegerField(
        blank=False,
        null=False,
        validators=(
            validate_car_year,
        ),
    )

    image_url = models.URLField(
        unique=True,
        blank=False,
        null=False,
        verbose_name="Image URL",
        error_messages={
            "unique": "This image URL is already in use! Provide a new one."
        },
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=(
            MinValueValidator(MIN_CAR_PRICE),
        ),
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name="cars",
    )


