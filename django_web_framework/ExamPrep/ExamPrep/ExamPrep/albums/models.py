from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from ExamPrep.profiles.models import Profile


class Album(models.Model):
    class GenreChoices(models.TextChoices):
        POP_MUSIC = "Pop Music", _("Pop Music"),
        JAZZ_MUSIC = "Jazz Music", _("Jazz Music")
        RNB_MUSIC = "R&B Music", _("R&B Music")
        ROCK_MUSIC = "Rock Music", _("Rock Music")
        COUNTRY_MUSIC = "Country Music", _("Country Music")
        DANCE_MUSIC = "Dance Music", _("Dance Music")
        HIP_HOP_MUSIC = "Hip Hop Music", _("Hip Hop Music")
        OTHER = "Other", _("Other")

    MAX_ALBUM_NAME_LENGTH = 30
    MAX_ARTIST_NAME_LENGTH = 30
    MAX_GENRE_LENGTH = 30
    MIN_PRICE = 0.0

    name = models.CharField(
        max_length=MAX_ALBUM_NAME_LENGTH,
        blank=False,
        null=False,
        unique=True,
        verbose_name="Album Name"
    )

    artist_name = models.CharField(
        max_length=MAX_ARTIST_NAME_LENGTH,
        blank=True,
        null=True,
        verbose_name="Artist"
    )

    genre = models.CharField(
        max_length=MAX_GENRE_LENGTH,
        choices=GenreChoices.choices,
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description"
    )

    image_url = models.URLField(
        blank=False,
        null=False,
        verbose_name="Image URL"
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(MIN_PRICE)
        ],
        verbose_name="Price"
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name="albums",
    )
