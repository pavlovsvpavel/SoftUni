import os
from datetime import timedelta, date

import django
from django.utils.timezone import now

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Artist, Song, Product, Review, Driver, DrivingLicense, Owner, Car, Registration


# Problem 1
def show_all_authors_with_their_books():
    result = []

    for c_author in Author.objects.all().order_by('id'):
        all_books = c_author.book_set.all()

        if not all_books:
            continue

        else:
            result.append(
                f"{c_author.name} has written - "
                f"{', '.join(b.title for b in all_books)}!"
            )

    return '\n'.join(result)


def delete_all_authors_without_books():
    # for c_author in Author.objects.all():
    #     all_books = c_author.book_set.all()
    #
    #     if not all_books:
    #         c_author.delete()

    Author.objects.filter(book__isnull=True).delete()


# Create authors
# author1 = Author.objects.create(name="J.K. Rowling")
# author2 = Author.objects.create(name="George Orwell")
# author3 = Author.objects.create(name="Harper Lee")
# author4 = Author.objects.create(name="Mark Twain")
#
# # Create books associated with the authors
# book1 = Book.objects.create(
#     title="Harry Potter and the Philosopher's Stone",
#     price=19.99,
#     author=author1
# )
# book2 = Book.objects.create(
#     title="1984",
#     price=14.99,
#     author=author2
# )
#
# book3 = Book.objects.create(
#     title="To Kill a Mockingbird",
#     price=12.99,
#     author=author3
# )
#
# # Display authors and their books
# authors_with_books = show_all_authors_with_their_books()
# print(authors_with_books)
#
# # Delete authors without books
# delete_all_authors_without_books()
# print(Author.objects.count())


# Problem 2
def add_song_to_artist(artist_name: str, song_title: str):
    # artist = None
    # song = None
    # for c_artist in Artist.objects.all():
    #     if c_artist.name == artist_name:
    #         artist = c_artist
    #
    # for c_song in Song.objects.all():
    #     if c_song.title == song_title:
    #         song = c_song

    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name: str):
    artist = Artist.objects.get(name=artist_name)

    return artist.songs.order_by('-id')

    # for c_artist in Artist.objects.all():
    #     if c_artist.name == artist_name:
    #         return c_artist.songs.order_by('-id')


def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)

    # for c_artist in Artist.objects.all():
    #     if c_artist.name == artist_name:
    #         for c_song in c_artist.songs.all():
    #             if c_song.title == song_title:
    #                 c_song.delete()


# Create artists
# artist1 = Artist.objects.create(name="Daniel Di Angelo")
# artist2 = Artist.objects.create(name="Indila")
#
# # Create songs
# song1 = Song.objects.create(title="Lose Face")
# song2 = Song.objects.create(title="Tourner Dans Le Vide")
# song3 = Song.objects.create(title="Loyalty")

# Add a song to an artist
# add_song_to_artist("Daniel Di Angelo", "Lose Face")
# add_song_to_artist("Daniel Di Angelo", "Loyalty")
# add_song_to_artist("Indila", "Tourner Dans Le Vide")
# #
# # Get all songs by a specific artist
# songs = get_songs_by_artist("Daniel Di Angelo")
# for song in songs:
#     print(f"Daniel Di Angelo: {song.title}")
# #
# # # Get all songs by a specific artist
# songs = get_songs_by_artist("Indila")
# for song in songs:
#     print(f"Indila: {song.title}")

# # Remove a song from an artist
# remove_song_from_artist("Daniel Di Angelo", "Lose Face")
# #
# # # Check if the song is removed
# songs = get_songs_by_artist("Daniel Di Angelo")
# #
# for song in songs:
#     print(f"Songs by Daniel Di Angelo after removal: {song.title}")


# Problem 3
def calculate_average_rating_for_product_by_name(product_name: str):
    ratings = Review.objects.filter(product__name=product_name).values_list('rating', flat=True)

    try:
        avg_rating = sum(ratings) / len(ratings)

    except ZeroDivisionError:
        avg_rating = 0

    return avg_rating


def get_reviews_with_high_ratings(threshold: int):
    reviews = Review.objects.filter(rating__gte=threshold)

    return reviews


def get_products_with_no_reviews():
    products = Product.objects.filter(reviews__isnull=True).order_by('-name')

    return products


def delete_products_without_reviews():
    get_products_with_no_reviews().delete()
    # for c_product in Product.objects.all():
    #     reviews = c_product.reviews.all()
    #     if not reviews:
    #         c_product.delete()


# # Create some products
# product1 = Product.objects.create(name="Laptop")
# product2 = Product.objects.create(name="Smartphone")
# product3 = Product.objects.create(name="Headphones")
# product4 = Product.objects.create(name="PlayStation 5")
#
# # Create some reviews for products
# review1 = Review.objects.create(description="Great laptop!", rating=5, product=product1)
# review2 = Review.objects.create(description="The laptop is slow!", rating=2, product=product1)
# review3 = Review.objects.create(description="Awesome smartphone!", rating=5, product=product2)
# #
# # # Run the function to get products without reviews
# products_without_reviews = get_products_with_no_reviews()
# print(f"Products without reviews: {', '.join([p.name for p in products_without_reviews])}")


# # Run the function to delete products without reviews
# delete_products_without_reviews()
# print(f"Products left: {Product.objects.count()}")
#
# Calculate and print the average rating
print(calculate_average_rating_for_product_by_name("Laptop"))
# print(get_reviews_with_high_ratings(2))


# Problem 4
def calculate_licenses_expiration_dates():
    result = []

    for c_license in DrivingLicense.objects.all().order_by('-license_number'):
        result.append(
            f"License with id: {c_license.license_number} "
            f"expires on {c_license.issue_date + timedelta(days=365)}!"
        )

    return '\n'.join(result)


def get_drivers_with_expired_licenses(due_date):
    result = []

    for c_driver in Driver.objects.all():
        if c_driver.drivinglicense.issue_date + timedelta(days=365) > due_date:
            result.append(c_driver)

    return result


# Create drivers
# driver1 = Driver.objects.create(first_name="Tanya", last_name="Petrova")
# driver2 = Driver.objects.create(first_name="Ivan", last_name="Yordanov")
# # Create licenses associated with drivers
# license1 = DrivingLicense.objects.create(license_number="123", issue_date=date(2022, 10, 6), driver=driver1)
# license2 = DrivingLicense.objects.create(license_number="456", issue_date=date(2022, 1, 1), driver=driver2)
#
# # # Calculate licenses expiration dates
# expiration_dates = calculate_licenses_expiration_dates()
# print(expiration_dates)
#
# # Get drivers with expired licenses
# drivers_with_expired_licenses = get_drivers_with_expired_licenses(date(2023, 1, 1))
# for driver in drivers_with_expired_licenses:
#     print(f"{driver.first_name} {driver.last_name} has to renew their driving license!")


# Problem 5
def register_car_by_owner(owner: Owner):
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True).first()

    car.owner = owner
    car.registration = registration
    car.save()

    registration.registration_date = date.today()
    registration.car = car
    registration.save()

    return (f"Successfully registered {car.model} to "
            f"{owner.name} with registration number {registration.registration_number}.")

# Create instances of the Owner model
# owner1 = Owner.objects.create(name='Ivelin Milchev')
# owner2 = Owner.objects.create(name='Alice Smith')

# # Create instances of the Car model and associate them with owners
# car1 = Car.objects.create(model='Citroen C5', year=2004)
# car2 = Car.objects.create(model='Honda Civic', year=2021)
#
# # Create instances of the Registration model for the cars
# registration1 = Registration.objects.create(registration_number='TX0044XA')
# registration2 = Registration.objects.create(registration_number='XYZ789')

# print(register_car_by_owner(owner1))
# print(register_car_by_owner(owner2))
