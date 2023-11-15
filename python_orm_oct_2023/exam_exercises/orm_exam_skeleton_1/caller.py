import os
import django
from django.db.models import Q, Avg, Count, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Director, Actor, Movie


# Problem 3
# print(Director.objects.get_directors_by_movies_count())


# Problem 4
def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ""

    if search_name and search_nationality:
        query = Q(full_name__icontains=search_name) & Q(nationality__icontains=search_nationality)

    elif search_name:
        query = Q(full_name__icontains=search_name)

    else:
        query = Q(nationality__icontains=search_nationality)

    matching_directors = Director.objects.filter(query).order_by('full_name')

    if not matching_directors:
        return ""

    result = []
    for director in matching_directors:
        result.append(f"Director: {director.full_name}, "
                      f"nationality: {director.nationality}, "
                      f"experience: {director.years_of_experience}")

    return '\n'.join(result)


# print(get_directors(search_name='W', search_nationality='Alabala'))
# print(get_directors(search_name=None, search_nationality='Bulg'))


def get_top_director():
    top_director = Director.objects.get_directors_by_movies_count().first()

    if not top_director:
        return ""

    return f"Top Director: {top_director.full_name}, movies: {top_director.count_movies}."


# print(get_top_director())


def get_top_actor():
    all_actors = (Actor.objects.prefetch_related('actor_movies__starring_actor').
                  annotate(count_movies=Count('movies'), movies_avg_rating=Avg('movies__rating')).
                  order_by('-count_movies', 'full_name'))

    top_actor = all_actors.first()

    if not top_actor or not top_actor.count_movies:
        return ""

    top_actor_movies = []
    for movie in top_actor.movies.all():
        top_actor_movies.append(movie.title)

    return (f"Top Actor: {top_actor.full_name}, "
            f"starring in movies: {', '.join(top_actor_movies)}, "
            f"movies average rating: {top_actor.movies_avg_rating:.1f}")


# print(get_top_actor())


# Problem 5
def get_actors_by_movies_count():
    actors = (Actor.objects.
              annotate(count_movies=Count('actor_movies')).
              order_by('-count_movies', 'full_name'))

    top_three_actors = actors[:3]

    if not top_three_actors or not top_three_actors[0].count_movies:
        return ""

    result = []
    for actor in top_three_actors:
        result.append(f"{actor.full_name}, participated in {actor.count_movies} movies")

    return '\n'.join(result)


# print(get_actors_by_movies_count())


def get_top_rated_awarded_movie():
    movie = (Movie.objects.
             select_related('starring_actor').
             prefetch_related('actors').
             filter(is_awarded=True).
             order_by('-rating', 'title').
             first())

    if movie is None:
        return ""

    if movie.starring_actor:
        starring_actor = movie.starring_actor.full_name

    else:
        starring_actor = "N/A"

    cast = []
    for actor in movie.actors.all().order_by('full_name'):
        cast.append(actor.full_name)

    return (f"Top rated awarded movie: {movie.title}, "
            f"rating: {movie.rating:.1f}. "
            f"Starring actor: {starring_actor}. "
            f"Cast: {', '.join(cast)}")


# print(get_top_rated_awarded_movie())


def increase_rating():
    query = Q(is_classic=True) & Q(rating__lt=10.0)

    movies = Movie.objects.filter(query)

    if not movies:
        return "No ratings increased."

    updated_movies = movies.update(rating=F('rating') + 0.1)

    return f"Rating increased for {updated_movies} movies."

# print(increase_rating())
