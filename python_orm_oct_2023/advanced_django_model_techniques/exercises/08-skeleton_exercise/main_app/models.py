from decimal import Decimal

from django.core.validators import MinValueValidator, RegexValidator, EmailValidator, URLValidator, MinLengthValidator
from django.db import models
from django.contrib.postgres.search import SearchVectorField
from main_app.validators import check_phone_number


class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[RegexValidator('^[a-zA-Z ]+$', 'Name can only contain letters and spaces')]
    )

    age = models.PositiveIntegerField(
        validators=[MinValueValidator(18, 'Age must be greater than 18')]
    )

    email = models.EmailField(
        validators=[EmailValidator()]
    )

    phone_number = models.CharField(
        max_length=13,
        validators=[check_phone_number]
    )

    website_url = models.URLField(
        validators=[URLValidator()]
    )


class BaseMedia(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        abstract = True
        ordering = ['-created_at', 'title']


class Book(BaseMedia):
    author = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(5, 'Author must be at least 5 characters long')]
    )
    isbn = models.CharField(
        max_length=20,
        unique=True,
        validators=[MinLengthValidator(6, 'ISBN must be at least 6 characters long')]
    )

    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Book'
        verbose_name_plural = 'Models of type - Book'


class Movie(BaseMedia):
    director = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(8, 'Director must be at least 8 characters long')]
    )

    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Movie'
        verbose_name_plural = 'Models of type - Movie'


class Music(BaseMedia):
    artist = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(9, 'Artist must be at least 9 characters long')]
    )

    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Music'
        verbose_name_plural = 'Models of type - Music'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_tax(self):
        return float(self.price) * 0.08

    def calculate_shipping_cost(self, weight: Decimal):
        return float(weight) * 2.00

    def format_product_name(self):
        return f"Product: {self.name}"


class DiscountedProduct(Product):
    class Meta:
        proxy = True

    def calculate_price_without_discount(self):
        return float(self.price) * 1.2

    def calculate_tax(self):
        return float(self.price) * 0.05

    def calculate_shipping_cost(self, weight: Decimal):
        return float(weight) * 1.50

    def format_product_name(self):
        return f"Discounted Product: {self.name}"


class RechargeEnergyMixin(models.Model):
    class Meta:
        abstract = True

    energy = models.PositiveIntegerField()

    def recharge_energy(self, amount: int):
        self.energy += amount

        if self.energy > 100:
            self.energy = 100

        self.save()


class Hero(RechargeEnergyMixin, models.Model):
    name = models.CharField(max_length=100)
    hero_title = models.CharField(max_length=100)

    def clean(self):
        if self.energy <= 0:
            return False

        return True


class SpiderHero(Hero):
    class Meta:
        proxy = True

    def swing_from_buildings(self):
        self.energy -= 80
        if not super().clean():
            return f"{self.name} as Spider Hero is out of web shooter fluid"

        self.save()

        return f"{self.name} as Spider Hero swings from buildings using web shooters"


class FlashHero(Hero):
    class Meta:
        proxy = True

    def run_at_super_speed(self):
        self.energy -= 65

        if not super().clean():
            return f"{self.name} as Flash Hero needs to recharge the speed force"

        self.save()

        return f"{self.name} as Flash Hero runs at lightning speed, saving the day"


class Document(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['search_vector']
                         )
        ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    search_vector = SearchVectorField(null=True)
