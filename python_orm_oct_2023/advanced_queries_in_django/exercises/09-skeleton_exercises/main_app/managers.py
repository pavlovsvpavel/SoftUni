from decimal import Decimal
from django.db import models
from django.db.models import Q, Count, Max, Min, Avg


class RealEstateListingManager(models.Manager):

    def by_property_type(self, property_type: str):
        query = Q(property_type=property_type)
        return self.filter(query)

    def in_price_range(self, min_price: Decimal, max_price: Decimal):
        query = Q(price__gte=min_price) & Q(price__lte=max_price)
        return self.filter(query)

    def with_bedrooms(self, bedrooms_count: int):
        query = Q(bedrooms=bedrooms_count)
        return self.filter(query)

    def popular_locations(self):
        return (self.values('location').
                annotate(num_of_locations=Count('id')).order_by('id')[:2])


class VideoGameManager(models.Manager):
    def games_by_genre(self, genre: str):
        query = Q(genre=genre)

        return self.filter(query)

    def recently_released_games(self, year: int):
        query = Q(release_year__gte=year)

        return self.filter(query)

    def highest_rated_game(self):
        highest_rating = self.aggregate(highest_rating=Max('rating'))['highest_rating']
        query = Q(rating=highest_rating)
        game_instance = self.get(query)

        return game_instance

    def lowest_rated_game(self):
        lowest_rating = self.aggregate(lowest_rating=Min('rating'))['lowest_rating']
        query = Q(rating=lowest_rating)
        game_instance = self.get(query)

        return game_instance

    def average_rating(self):
        avg_rating = self.aggregate(avg_rating=Avg('rating'))['avg_rating']

        return f"{avg_rating:.1f}"

