from datetime import timedelta
from decimal import Decimal

from django.db import models
from django.db.models import Count, Q, Max, Min, Avg, F
from django.db.models.functions import Round

from main_app.validators import video_game_rating, video_game_release_year


# Create your models here.
class RealEstateListingManager(models.Manager):
    @staticmethod
    def by_property_type(property_type: str):
        query = Q(property_type=property_type)
        return RealEstateListing.objects.filter(query)

    @staticmethod
    def in_price_range(min_price: Decimal, max_price: Decimal):
        query = Q(price__gte=min_price) & Q(price__lte=max_price)
        return RealEstateListing.objects.filter(query)

    @staticmethod
    def with_bedrooms(bedrooms_count: int):
        query = Q(bedrooms=bedrooms_count)
        return RealEstateListing.objects.filter(query)

    @staticmethod
    def popular_locations():
        return (RealEstateListing.objects.values('location').
                annotate(num_of_locations=Count('id')).order_by('id')[:2])


class VideoGameManager(models.Manager):
    @staticmethod
    def games_by_genre(genre: str):
        query = Q(genre=genre)
        return VideoGame.objects.filter(query)

    @staticmethod
    def recently_released_games(year: int):
        query = Q(release_year__gte=year)
        return VideoGame.objects.filter(query)

    @staticmethod
    def highest_rated_game():
        highest_rating = VideoGame.objects.aggregate(highest_rating=Max('rating'))['highest_rating']
        query = Q(rating=highest_rating)
        game_instance = VideoGame.objects.get(query)

        return game_instance

    @staticmethod
    def lowest_rated_game():
        lowest_rating = VideoGame.objects.aggregate(lowest_rating=Min('rating'))['lowest_rating']
        query = Q(rating=lowest_rating)
        game_instance = VideoGame.objects.get(query)

        return game_instance

    @staticmethod
    def average_rating():
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


class InvoiceMixin(models.Model):
    class Meta:
        abstract = True

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


class Invoice(InvoiceMixin):
    invoice_number = models.CharField(max_length=20, unique=True)
    billing_info = models.OneToOneField(BillingInfo, on_delete=models.CASCADE)


class Technology(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    technologies_used = models.ManyToManyField(Technology, related_name='projects')

    @staticmethod
    def get_programmers_with_technologies():
        query = Programmer.objects.prefetch_related('projects').all()

        return query


class Programmer(models.Model):
    name = models.CharField(max_length=100)
    projects = models.ManyToManyField(Project, related_name='programmers')

    @staticmethod
    def get_projects_with_technologies():
        query = Project.objects.prefetch_related('programmers__projects__technologies_used').all()

        return query


class TaskMixin(models.Model):
    class Meta:
        abstract = True

    @staticmethod
    def overdue_high_priority_tasks():
        query = (Q(priority='High') &
                 Q(is_completed=False) &
                 Q(completion_date__gt=F('creation_date')))

        return Task.objects.filter(query)

    @staticmethod
    def completed_mid_priority_tasks():
        query = (Q(priority='Medium') &
                 Q(is_completed=True))

        return Task.objects.filter(query)

    @staticmethod
    def search_tasks(query: str):
        query_filter = (Q(title__contains=query) |
                        Q(description__contains=query))

        return Task.objects.filter(query_filter)

    @staticmethod
    def recent_completed_tasks(days: int):
        new_date = F('creation_date') - timedelta(days)

        query = (Q(is_completed=True) &
                 Q(completion_date__gte=new_date))

        return Task.objects.filter(query)


class Task(TaskMixin):
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


class ExerciseMixin(models.Model):
    class Meta:
        abstract = True

    @staticmethod
    def get_long_and_hard_exercises():
        query = (Q(duration_minutes__gt=30) &
                 Q(difficulty_level__gte=10))

        return Exercise.objects.filter(query)

    @staticmethod
    def get_short_and_easy_exercises():
        query = (Q(duration_minutes__lt=15) &
                 Q(difficulty_level__lt=5))

        return Exercise.objects.filter(query)

    @staticmethod
    def get_exercises_within_duration(min_duration: int, max_duration: int):
        query = (Q(duration_minutes__gte=min_duration) &
                 Q(duration_minutes__lte=max_duration))

        return Exercise.objects.filter(query)

    @staticmethod
    def get_exercises_with_difficulty_and_repetitions(
            min_difficulty: int, min_repetitions: int):
        query = (Q(difficulty_level__gte=min_difficulty) &
                 Q(repetitions__gte=min_repetitions))

        return Exercise.objects.filter(query)


class Exercise(ExerciseMixin):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    difficulty_level = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()
