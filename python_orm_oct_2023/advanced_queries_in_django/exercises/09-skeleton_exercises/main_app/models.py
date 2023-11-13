from datetime import timedelta

from django.db import models
from django.db.models import Q, F

from main_app.managers import RealEstateListingManager, VideoGameManager
from main_app.validators import video_game_rating, video_game_release_year


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

    def get_programmers_with_technologies(self):
        query = self.programmers.prefetch_related('projects__technologies_used')

        return query


class Programmer(models.Model):
    name = models.CharField(max_length=100)
    projects = models.ManyToManyField(Project, related_name='programmers')

    def get_projects_with_technologies(self):
        query = self.projects.prefetch_related('technologies_used')

        return query


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

    @classmethod
    def overdue_high_priority_tasks(cls):
        query = (Q(priority='High') &
                 Q(is_completed=False) &
                 Q(completion_date__gt=F('creation_date')))

        return cls.objects.filter(query)

    @classmethod
    def completed_mid_priority_tasks(cls):
        query = (Q(priority='Medium') &
                 Q(is_completed=True))

        return cls.objects.filter(query)

    @classmethod
    def search_tasks(cls, query: str):
        query_filter = (Q(title__contains=query) |
                        Q(description__contains=query))

        return cls.objects.filter(query_filter)

    def recent_completed_tasks(self, days: int):
        new_date = self.creation_date - timedelta(days)

        query = (Q(is_completed=True) &
                 Q(completion_date__gte=new_date))

        return Task.objects.filter(query)


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    difficulty_level = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()

    @classmethod
    def get_long_and_hard_exercises(cls):
        query = (Q(duration_minutes__gt=30) &
                 Q(difficulty_level__gte=10))

        return cls.objects.filter(query)

    @classmethod
    def get_short_and_easy_exercises(cls):
        query = (Q(duration_minutes__lt=15) &
                 Q(difficulty_level__lt=5))

        return cls.objects.filter(query)

    @classmethod
    def get_exercises_within_duration(cls, min_duration: int, max_duration: int):
        query = (Q(duration_minutes__gte=min_duration) &
                 Q(duration_minutes__lte=max_duration))

        return cls.objects.filter(query)

    @classmethod
    def get_exercises_with_difficulty_and_repetitions(
            cls, min_difficulty: int, min_repetitions: int):
        query = (Q(difficulty_level__gte=min_difficulty) &
                 Q(repetitions__gte=min_repetitions))

        return cls.objects.filter(query)
