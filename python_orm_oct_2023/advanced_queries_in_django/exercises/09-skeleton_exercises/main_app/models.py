from decimal import Decimal

from django.db import models
from django.db.models import Count, Q, Max, Min, Avg, F
from django.db.models.functions import Round

from main_app.validators import video_game_rating, video_game_release_year


# Create your models here.
class RealEstateListingManager(models.Manager):
    def by_property_type(self, property_type: str):
        query = Q(property_type=property_type)
        return RealEstateListing.objects.filter(query)

    def in_price_range(self, min_price: Decimal, max_price: Decimal):
        query = Q(price__gte=min_price) & Q(price__lte=max_price)
        return RealEstateListing.objects.filter(query)

    def with_bedrooms(self, bedrooms_count: int):
        query = Q(bedrooms=bedrooms_count)
        return RealEstateListing.objects.filter(query)

    def popular_locations(self):
        return (RealEstateListing.objects.values('location').
                annotate(num_of_locations=Count('id')).order_by('id')[:2])


class VideoGameManager(models.Manager):
    def games_by_genre(self, genre: str):
        query = Q(genre=genre)
        return VideoGame.objects.filter(query)

    def recently_released_games(self, year: int):
        query = Q(release_year__gte=year)
        return VideoGame.objects.filter(query)

    def highest_rated_game(self):
        highest_rating = VideoGame.objects.aggregate(highest_rating=Max('rating'))['highest_rating']
        query = Q(rating=highest_rating)
        game_instance = VideoGame.objects.get(query)

        return game_instance

    def lowest_rated_game(self):
        lowest_rating = VideoGame.objects.aggregate(lowest_rating=Min('rating'))['lowest_rating']
        query = Q(rating=lowest_rating)
        game_instance = VideoGame.objects.get(query)

        return game_instance

    def average_rating(self):
        avg_rating = VideoGame.objects.aggregate(avg_rating=Round(Avg('rating'), 1))['avg_rating']

        return avg_rating

        # avg_ratings = VideoGame.objects.annotate(avg_rating=Round(Avg('rating'), 1))
        #
        # return avg_ratings.order_by('-avg_rating')


class RealEstateListing(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('House', 'House'),
        ('Flat', 'Flat'),
        ('Villa', 'Villa'),
        ('Cottage', 'Cottage'),
        ('Studio', 'Studio'),
    ]

    property_type = models.CharField(max_length=100, choices=PROPERTY_TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    location = models.CharField(max_length=100)

    objects = RealEstateListingManager()


class VideoGame(models.Model):
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('RPG', 'RPG'),
        ('Adventure', 'Adventure'),
        ('Sports', 'Sports'),
        ('Strategy', 'Strategy'),
    ]

    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    release_year = models.PositiveIntegerField(
        validators=[video_game_release_year]
    )
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[video_game_rating]
    )

    objects = VideoGameManager()

    def __str__(self):
        return f"{self.title}"


class BillingInfo(models.Model):
    address = models.CharField(max_length=200)


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    billing_info = models.OneToOneField(BillingInfo, on_delete=models.CASCADE)

    @staticmethod
    def get_invoices_with_prefix(prefix):
        query = Invoice.objects.filter(Q(invoice_number__startswith=prefix))

        return query

    @staticmethod
    def get_invoices_sorted_by_number():
        query = Invoice.objects.order_by('invoice_number')

        return query

    @staticmethod
    def get_invoice_with_billing_info(invoice_number: str):
        query = Invoice.objects.get(invoice_number=invoice_number)

        return query


class Technology(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    technologies_used = models.ManyToManyField(Technology, related_name='projects')


class Programmer(models.Model):
    name = models.CharField(max_length=100)
    projects = models.ManyToManyField(Project, related_name='programmers')


class Task(models.Model):
    PRIORITIES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITIES)
    is_completed = models.BooleanField(default=False)
    creation_date = models.DateField()
    completion_date = models.DateField()


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    difficulty_level = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()
