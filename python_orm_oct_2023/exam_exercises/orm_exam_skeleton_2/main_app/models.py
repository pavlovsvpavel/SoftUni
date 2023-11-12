from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from django.db import models

from main_app.managers import ProfileManager
from main_app.mixins import CreationDateTimeMixin


class Profile(CreationDateTimeMixin):
    full_name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(2, 'Name must be at least 2 characters long.'),
            MaxLengthValidator(100, 'Name cannot exceed 100 characters.')
        ]
    )

    email = models.EmailField()

    phone_number = models.CharField(
        max_length=15,
        validators=[
            MaxLengthValidator(15, 'Phone number cannot exceed 15 characters.')
        ]
    )

    address = models.TextField()

    is_active = models.BooleanField(
        default=True
    )

    objects = ProfileManager()

    def __str__(self):
        return f"{self.full_name}"


class Product(CreationDateTimeMixin):
    name = models.CharField(
        max_length=100,
        validators=[
            MaxLengthValidator(100, 'Name cannot exceed 100 characters.')
        ]
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(0.01, 'Value should be greater than or equal to 0.01')
        ]
    )

    in_stock = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0, 'Value should be greater than 0')
        ]
    )

    is_available = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f"{self.name}"


class Order(CreationDateTimeMixin):
    profile = models.ForeignKey(
        to='Profile',
        on_delete=models.CASCADE,
        related_name='profile_orders'
    )

    products = models.ManyToManyField(
        to='Product',
        related_name='product_orders'
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(0.01, 'Value should be greater than or equal to 0.01')
        ]
    )

    is_completed = models.BooleanField(
        default=False
    )
