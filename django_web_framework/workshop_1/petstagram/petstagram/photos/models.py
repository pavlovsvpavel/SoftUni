from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_photo_size


class PetPhoto(models.Model):
    MAX_LENGTH_DESCRIPTION = 300
    MIN_LENGTH_DESCRIPTION = 10
    MAX_IMAGE_SIZE_LOCATION = 30

    photo = models.ImageField(
        upload_to='pet_photos/',
        validators=[
            validate_photo_size,
        ]
    )

    description = models.TextField(
        max_length=MAX_LENGTH_DESCRIPTION,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(MIN_LENGTH_DESCRIPTION, message='Description must be more than 10 characters')
        ]
    )

    location = models.CharField(
        max_length=MAX_IMAGE_SIZE_LOCATION,
        blank=False,
        null=False
    )

    pets = models.ManyToManyField(
        to=Pet,
        blank=True,
        related_name='pet_photos',
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)


