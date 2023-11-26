import os
import django
from django.db.models import Q, Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Article, Review


# print(Author.objects.get_authors_by_article_count())

def get_authors(search_name=None, search_email=None):
    if search_name is None and search_email is None:
        return ""

    query = Q()

    if search_name and search_email:
        query = (Q(full_name__icontains=search_name) &
                 Q(email__icontains=search_email))

    elif search_name:
        query = Q(full_name__icontains=search_name)

    else:
        query = Q(email__icontains=search_email)

    authors = Author.objects.filter(query).order_by('-full_name')

    if not authors:
        return ""

    result = []
    for author in authors:
        result.append(
            f"Author: {author.full_name}, "
            f"email: {author.email}, "
            f"status: {'Banned' if author.is_banned else 'Not Banned'}"
        )

    return "\n".join(result)


# print(get_authors('A', ''))


def get_top_publisher():
    top_author = (Author.objects.get_authors_by_article_count().
                  filter(num_of_articles__gt=0).
                  first())

    if not top_author:
        return ""

    return f"Top Author: {top_author.full_name} with {top_author.num_of_articles} published articles."


# print(get_top_publisher())


def get_top_reviewer():
    top_reviewer = (Author.objects.
                    annotate(num_of_reviews=Count('author_reviews')).
                    filter(num_of_reviews__gt=0).
                    order_by('-num_of_reviews', 'email').
                    first())

    if not top_reviewer:
        return ""

    return (f"Top Reviewer: {top_reviewer.full_name} "
            f"with {top_reviewer.num_of_reviews} published reviews.")


# print(get_top_reviewer())


def get_latest_article():
    latest_article = (
        Article.objects.
        prefetch_related('authors', 'article_reviews').
        annotate(num_of_reviews=Count('article_reviews'),
                 average_rating=Avg('article_reviews__rating')).last())

    if not latest_article:
        return ""

    authors = []
    for author in latest_article.authors.all():
        authors.append(author.full_name)

    rating = latest_article.average_rating if latest_article.average_rating is not None else 0

    return (f"The latest article is: {latest_article.title}. "
            f"Authors: {', '.join(authors)}. "
            f"Reviewed: {latest_article.num_of_reviews} times. "
            f"Average Rating: {rating:.2f}.")


# print(get_latest_article())


def get_top_rated_article():
    top_rated_article = (
        Article.objects.prefetch_related('article_reviews').
        annotate(num_of_reviews=Count('article_reviews'),
                 avg_rating=Avg('article_reviews__rating')).
        filter(num_of_reviews__gt=0).
        order_by('-avg_rating', 'title').
        first())

    if not top_rated_article:
        return ""

    return (f"The top-rated article is: {top_rated_article.title}, "
            f"with an average rating of {top_rated_article.avg_rating:.2f}, "
            f"reviewed {top_rated_article.num_of_reviews} times.")


# print(get_top_rated_article())


def ban_author(email=None):
    author = (Author.objects.
              prefetch_related('author_reviews').
              annotate(num_of_reviews=Count('author_reviews')).
              filter(email__exact=email).first())

    if not author:
        return "No authors banned."

    author.is_banned = True
    author.save()

    for review in author.author_reviews.all():
        review.delete()

    return (f"Author: {author.full_name} is banned! "
            f"{author.num_of_reviews} reviews deleted.")

# print(ban_author('Author 6'))
