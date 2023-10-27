import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery, Laptop, ChessPlayer


# Problem 1
def show_highest_rated_art():
    highest_rated = ArtworkGallery.objects.all().order_by('-rating', 'id').first()

    return f"{highest_rated.art_name} is the highest-rated art with a {highest_rated.rating} rating!"


def bulk_create_arts(first_art, second_art):
    ArtworkGallery.objects.bulk_create([first_art, second_art])


def delete_negative_rated_arts():
    ArtworkGallery.objects.filter(rating__lt=0).delete()


# artwork1 = ArtworkGallery(artist_name="Vincent van Gogh", art_name="Starry Night", rating=4, price=1200000.0)
# artwork2 = ArtworkGallery(artist_name="Leonardo da Vinci", art_name="Mona Lisa", rating=5, price=1500000.0)
# bulk_create_arts(artwork1, artwork2)

# print(show_highest_rated_art())
# print(ArtworkGallery.objects.all())


# Problem 2
def show_the_most_expensive_laptop():
    most_expensive_laptop = Laptop.objects.order_by('-price', 'id').first()

    return (f"{most_expensive_laptop.brand} is the most expensive laptop "
            f"available for {most_expensive_laptop.price}$!")


def bulk_create_laptops(*args):
    Laptop.objects.bulk_create(*args)


def update_to_512_GB_storage():
    Laptop.objects.filter(brand__in=['Asus', 'Lenovo']).update(storage=512)


def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=['Apple', 'Dell', 'Acer']).update(memory=16)


def update_operation_systems():
    # Laptop.objects.filter(brand='Asus').update(
    #     operation_system='Windows'
    # )
    #
    # Laptop.objects.filter(brand='Apple').update(
    #     operation_system='Mac OS'
    # )
    #
    # Laptop.objects.filter(brand__in=['Acer', 'Dell']).update(
    #     operation_system='Linux'
    # )
    #
    # Laptop.objects.filter(brand='Lenovo').update(
    #     operation_system='Chrome OS'
    # )

    for c_laptop in Laptop.objects.all():
        brand = c_laptop.brand

        match brand:
            case 'Asus':
                Laptop.objects.filter(brand='Asus').update(operation_system='Windows')
            case 'Apple':
                Laptop.objects.filter(brand='Apple').update(operation_system='MacOS')
            case 'Acer' | 'Dell':
                Laptop.objects.filter(brand__in=['Acer', 'Dell']).update(operation_system='Linux')
            case 'Lenovo':
                Laptop.objects.filter(brand='Lenovo').update(operation_system='Chrome OS')


def delete_inexpensive_laptops():
    Laptop.objects.all().filter(price__lt=1200).delete()


# Create three instances of Laptop
# laptop1 = Laptop(
#     brand='Asus',
#     processor='Intel Core i5',
#     memory=8,
#     storage=256,
#     operation_system='Windows',
#     price=899.99
# )
#
# laptop2 = Laptop(
#     brand='Apple',
#     processor='Apple M1',
#     memory=16,
#     storage=512,
#     operation_system='MacOS',
#     price=1399.99
#
# )
#
# laptop3 = Laptop(
#     brand='Lenovo',
#     processor='AMD Ryzen 7',
#     memory=12,
#     storage=512,
#     operation_system='Linux',
#     price=999.99,
# )


# laptops_to_create = [laptop1, laptop2, laptop3]
# bulk_create_laptops(laptops_to_create)

# print(show_the_most_expensive_laptop())

# Execute the following functions
# update_to_512_GB_storage()
# update_operation_systems()

# delete_inexpensive_laptops()

# Retrieve 2 laptops from the database
# asus_laptop = Laptop.objects.filter(brand__exact='Asus').get()
# lenovo_laptop = Laptop.objects.filter(brand__exact='Lenovo').get()
#
# print(asus_laptop.storage)
# print(lenovo_laptop.operation_system)

# Problem 3
def bulk_create_chess_players(*args):
    ChessPlayer.objects.bulk_create(*args)


def delete_chess_players():
    ChessPlayer.objects.filter(title='no title').delete()


def change_chess_games_won():
    ChessPlayer.objects.filter(title='GM').update(games_won=30)


def change_chess_games_lost():
    ChessPlayer.objects.filter(title='no title').update(games_lost=25)


def change_chess_games_drawn():
    ChessPlayer.objects.update(games_drawn=10)


def grand_chess_title_GM():
    ChessPlayer.objects.filter(rating__gte=2400).update(title='GM')


def grand_chess_title_IM():
    ChessPlayer.objects.filter(rating__range=(2300, 2399)).update(title='IM')


def grand_chess_title_FM():
    ChessPlayer.objects.filter(rating__range=(2200, 2299)).update(title='FM')


def grand_chess_title_regular_player():
    ChessPlayer.objects.filter(rating__lte=2199).update(title='regular player')

# Create two instances of ChessPlayer
# player1 = ChessPlayer(
#     username='Player1',
#     title='no title',
#     rating=2200,
#     games_played=50,
#     games_won=20,
#     games_lost=25,
#     games_drawn=5,
# )
#
# player2 = ChessPlayer(
#     username='Player2',
#     title='IM',
#     rating=2350,
#     games_played=80,
#     games_won=40,
#     games_lost=25,
#     games_drawn=15,
# )

# Call the bulk_create_chess_players function
# bulk_create_chess_players([player1, player2])

# Call the delete_chess_players function
# delete_chess_players()

# Check that the players are deleted
# print("Number of Chess Players after deletion:", ChessPlayer.objects.count())


# Problem 4
