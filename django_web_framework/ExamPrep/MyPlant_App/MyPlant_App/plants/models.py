from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from MyPlant_App.plants.validators import validate_plant_name
from MyPlant_App.profiles.models import Profile


class Plant(models.Model):
    MIN_NAME_LENGTH = 2
    MAX_NAME_LENGTH = 20

    class PlantTypesChoices(models.TextChoices):
        OUTDOOR = "Outdoor Plants", _("Outdoor Plants"),
        INDOOR = "Indoor Plants", _("Indoor Plants")

    plant_type = models.CharField(
        max_length=14,
        choices=PlantTypesChoices,
        verbose_name="Type"
    )

    name = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(MIN_NAME_LENGTH),
            MaxLengthValidator(MAX_NAME_LENGTH),
            validate_plant_name
        ]
    )

    image_url = models.URLField(
        blank=False,
        null=False,
        verbose_name="Image URL",
    )

    description = models.TextField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        blank=False,
        null=False,
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name="plants",
    )
