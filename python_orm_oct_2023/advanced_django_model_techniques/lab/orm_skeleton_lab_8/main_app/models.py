from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
from django.db import models


class Restaurant(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(
                2, "Name must be at least 2 characters long."
            ),
            MaxLengthValidator(
                100, "Name cannot exceed 100 characters."
            )
        ]
    )
    location = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(
                2, "Location must be at least 2 characters long."
            ),
            MaxLengthValidator(
                200, "Location cannot exceed 200 characters."
            )
        ]
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[
            MinValueValidator(
                0, "Rating must be at least 0.00."
            ),
            MaxValueValidator(
                5, "Rating cannot exceed 5.00."
            )
        ]
    )


def validate_menu_categories(value):
    categories = ["Appetizers", "Main Course", "Desserts"]

    matches = 0
    for el in categories:
        if value.lower().find(el.lower()) > 0:
            matches += 1

    if matches < len(categories):
        raise ValidationError(
            'The menu must include each of the categories "Appetizers", "Main Course", "Desserts".'
        )


class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(
        validators=[validate_menu_categories]
    )
    restaurant = models.ForeignKey(
        to='Restaurant',
        on_delete=models.CASCADE,
        related_name='menus'
    )


class ReviewMixin(models.Model):
    reviewer_name = models.CharField(max_length=100)
    review_content = models.TextField()
    rating = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(5)
        ]
    )

    class Meta:
        abstract = True
        ordering = ['-rating']


class RestaurantReview(ReviewMixin):
    restaurant = models.ForeignKey(
        to='Restaurant',
        on_delete=models.CASCADE,
    )

    class Meta(ReviewMixin.Meta):
        abstract = True
        verbose_name = 'Restaurant Review'
        verbose_name_plural = 'Restaurant Reviews'
        unique_together = ['reviewer_name', 'restaurant']


class RegularRestaurantReview(RestaurantReview):
    pass


class FoodCriticRestaurantReview(RestaurantReview):
    food_critic_cuisine_area = models.CharField(
        max_length=100
    )

    class Meta(RestaurantReview.Meta):
        verbose_name = 'Food Critic Review'
        verbose_name_plural = 'Food Critic Reviews'


class MenuReview(ReviewMixin):
    menu = models.ForeignKey(
        to='Menu',
        on_delete=models.CASCADE,
    )

    class Meta(ReviewMixin.Meta):
        verbose_name = 'Menu Review'
        verbose_name_plural = 'Menu Reviews'
        unique_together = ['reviewer_name', 'menu']
        indexes = [
            models.Index(fields=['menu'], name='main_app_menu_review_menu_id')
        ]
