from django.db import models

from petstagram.photos.models import PetPhoto


class Comment(models.Model):
    MAX_LENGTH_COMMENT = 300
    comment = models.TextField(
        max_length=MAX_LENGTH_COMMENT,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    photo = models.ForeignKey(
        to=PetPhoto,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name='comments'
    )

    class Meta:
        ordering = ("-created_at",)


class PhotoLike(models.Model):
    photo = models.ForeignKey(
        to=PetPhoto,
        on_delete=models.DO_NOTHING,
    )
