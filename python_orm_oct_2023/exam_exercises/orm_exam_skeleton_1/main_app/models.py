from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Count


class DirectorManager(models.Manager):

    def get_directors_by_movies_count(self):
        directors_movies = (
            self.annotate(count_movies=Count('director_movies')).
            order_by('-count_movies', 'full_name')
        )

        return directors_movies


class Person(models.Model):
    class Meta:
        abstract = True

    full_name = models.CharField(
        max_length=120,
        validators=[
            MinLengthValidator(2, 'Name must be at least 2 characters long.'),
            MaxLengthValidator(120, 'Name cannot exceed 120 characters.')
        ]
    )

    birth_date = models.DateField(
        default='1900-01-01'
    )

    nationality = models.CharField(
        max_length=50,
        validators=[MaxLengthValidator(50, 'Nationality cannot exceed 50 characters.')],
        default='Unknown'
    )

    def __str__(self):
        return self.full_name


class Director(Person):
    years_of_experience = models.SmallIntegerField(
        validators=[MinValueValidator(0, 'Years of experience cannot be negative.')],
        default=0
    )

    objects = DirectorManager()


class Actor(Person):
    is_awarded = models.BooleanField(
        default=False
    )

    last_updated = models.DateTimeField(
        auto_now=True
    )


class Movie(models.Model):
    class GenreChoices(models.TextChoices):
        ACTION = ('Action', 'Action')
        COMEDY = ('Comedy', 'Comedy')
        DRAMA = ('Drama', 'Drama')
        OTHER = ('Other', 'Other')

    title = models.CharField(
        max_length=150,
        validators=[
            MinLengthValidator(5, 'Title must be at least 5 characters long.'),
            MaxLengthValidator(150, 'Title cannot exceed 150 characters.')
        ]
    )

    release_date = models.DateField()
    storyline = models.TextField(
        null=True,
        blank=True
    )

    genre = models.CharField(
        max_length=6,
        validators=[
            MaxLengthValidator(6, 'Genre cannot exceed 6 characters.')
        ],
        default='Other',
        choices=GenreChoices.choices,
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0)
        ],
        default=0.0,
    )

    is_classic = models.BooleanField(
        default=False,
    )

    is_awarded = models.BooleanField(
        default=False
    )

    last_updated = models.DateTimeField(
        auto_now=True,
    )

    director = models.ForeignKey(
        to='Director',
        on_delete=models.CASCADE,
        related_name='director_movies'
    )

    starring_actor = models.ForeignKey(
        to='Actor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='movies'
    )

    actors = models.ManyToManyField(
        to='Actor',
        related_name='actor_movies'
    )

    def __str__(self):
        return self.title
