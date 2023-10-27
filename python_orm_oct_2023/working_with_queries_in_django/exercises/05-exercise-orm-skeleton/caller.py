import os
import django
from django.db.models import Q

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery, Laptop, ChessPlayer, Meal, Dungeon, Workout


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
def set_new_chefs():
    for c_meal in Meal.objects.all():
        meal = c_meal.meal_type

        match meal:
            case 'Breakfast':
                Meal.objects.filter(meal_type='Breakfast').update(chef='Gordon Ramsay')
            case 'Lunch':
                Meal.objects.filter(meal_type='Lunch').update(chef='Julia Child')
            case 'Dinner':
                Meal.objects.filter(meal_type='Dinner').update(chef='Jamie Oliver')
            case 'Snack':
                Meal.objects.filter(meal_type='Snack').update(chef='Thomas Keller')


def set_new_preparation_times():
    for c_meal in Meal.objects.all():
        meal = c_meal.meal_type

        match meal:
            case 'Breakfast':
                Meal.objects.filter(meal_type='Breakfast').update(preparation_time='10 minutes')
            case 'Lunch':
                Meal.objects.filter(meal_type='Lunch').update(preparation_time='12 minutes')
            case 'Dinner':
                Meal.objects.filter(meal_type='Dinner').update(preparation_time='15 minutes')
            case 'Snack':
                Meal.objects.filter(meal_type='Snack').update(preparation_time='5 minutes')


def update_low_calorie_meals():
    Meal.objects.filter(meal_type__in=['Breakfast', 'Dinner']).update(calories=400)


def update_high_calorie_meals():
    Meal.objects.filter(meal_type__in=['Lunch', 'Snack']).update(calories=700)


def delete_lunch_and_snack_meals():
    Meal.objects.filter(meal_type__in=['Lunch', 'Snack']).delete()


# Create two instances of the Meal model
# meal1 = Meal.objects.create(
#     name="Pancakes",
#     meal_type="Breakfast",
#     preparation_time="20 minutes",
#     difficulty=3,
#     calories=350,
#     chef="Jane",
# )
#
# meal2 = Meal.objects.create(
#     name="Spaghetti Bolognese",
#     meal_type="Dinner",
#     preparation_time="45 minutes",
#     difficulty=4,
#     calories=550,
#     chef="Sarah",
# )
# # Test the set_new_chefs function
# set_new_chefs()
#
# # Test the set_new_preparation_times function
# set_new_preparation_times()
#
# # Refreshes the instances
# meal1.refresh_from_db()
# meal2.refresh_from_db()
#
# # Print the updated meal information
# print("Meal 1 Chef:", meal1.chef)
# print("Meal 1 Preparation Time:", meal1.preparation_time)
# print("Meal 2 Chef:", meal2.chef)
# print("Meal 2 Preparation Time:", meal2.preparation_time)


# Problem 5
def show_hard_dungeons():
    hard_dungeons = Dungeon.objects.filter(difficulty='Hard').order_by('-location')

    result = [f"{dun.name} is guarded by {dun.boss_name} who has {dun.boss_health} health points!"
              for dun in hard_dungeons]

    return "\n".join(result)


def bulk_create_dungeons(*args):
    Dungeon.objects.bulk_create(*args)


def update_dungeon_names():
    for c_dungeon in Dungeon.objects.all():
        dungeon_difficulty = c_dungeon.difficulty

        match dungeon_difficulty:
            case 'Easy':
                Dungeon.objects.filter(difficulty='Easy').update(name='The Erased Thombs')
            case 'Medium':
                Dungeon.objects.filter(difficulty='Medium').update(name='The Coral Labyrinth')
            case 'Hard':
                Dungeon.objects.filter(difficulty='Hard').update(name='The Lost Haunt')


def update_dungeon_bosses_health():
    Dungeon.objects.exclude(difficulty='Easy').update(boss_health=500)


def update_dungeon_recommended_levels():
    for c_dungeon in Dungeon.objects.all():
        dungeon_difficulty = c_dungeon.difficulty

        match dungeon_difficulty:
            case 'Easy':
                Dungeon.objects.filter(difficulty='Easy').update(recommended_level=25)
            case 'Medium':
                Dungeon.objects.filter(difficulty='Medium').update(recommended_level=50)
            case 'Hard':
                Dungeon.objects.filter(difficulty='Hard').update(recommended_level=75)


def update_dungeon_rewards():
    for c_dungeon in Dungeon.objects.all():
        boos_health = c_dungeon.boss_health
        location = c_dungeon.location

        if boos_health == 500:
            Dungeon.objects.filter(boss_health=500).update(reward='1000 Gold')

        if location.startswith('E'):
            Dungeon.objects.filter(location__startswith='E').update(reward='New dungeon unlocked')

        if location.endswith('s'):
            Dungeon.objects.filter(location__endswith='s').update(reward='Dragonheart Amulet')

        # match (boos_health, location):
        #     case (500, location):
        #         Dungeon.objects.filter(boss_health=500).update(reward='1000 Gold')
        #     case (boos_health, location) if location.startswith('E'):
        #         Dungeon.objects.filter(location__startswith='E').update(reward='New dungeon unlocked')
        #     case (boos_health, location) if location.endswith('s'):
        #         Dungeon.objects.filter(location__endswith='s').update(reward='Dragonheart Amulet')


def set_new_locations():
    for c_dungeon in Dungeon.objects.all():
        rec_level = c_dungeon.recommended_level

        match rec_level:
            case 25:
                Dungeon.objects.filter(recommended_level=25).update(location='Enchanted Maze')
            case 50:
                Dungeon.objects.filter(recommended_level=50).update(location='Grimstone Mines')
            case 75:
                Dungeon.objects.filter(recommended_level=75).update(location='Shadowed Abyss')


# # Create two instances
# dungeon1 = Dungeon(
#     name="Dungeon 1",
#     boss_name="Boss 1",
#     boss_health=1000,
#     recommended_level=75,
#     reward="Gold",
#     location="Eternal Hell",
#     difficulty="Hard",
# )
#
# dungeon2 = Dungeon(
#     name="Dungeon 2",
#     boss_name="Boss 2",
#     boss_health=500,
#     recommended_level=25,
#     reward="Experience",
#     location="Crystal Caverns",
#     difficulty="Easy",
# )
#
# # Bulk save the instances
# bulk_create_dungeons([dungeon1, dungeon2])
#
# # Update boss's health
# update_dungeon_bosses_health()
#
# # Show hard dungeons
# hard_dungeons_info = show_hard_dungeons()
# print(hard_dungeons_info)
#
# # Change dungeon names based on difficulty
# update_dungeon_names()
# dungeons = Dungeon.objects.all()
# print(dungeons[0].name)
# print(dungeons[1].name)
#
# set_new_locations()
#
# # Change the dungeon rewards
# update_dungeon_rewards()
# dungeons = Dungeon.objects.all()
# print(dungeons[0].reward)
# print(dungeons[1].reward)


# Problem 6
def show_workouts():
    result = []
    filtered_workouts = (Workout.objects.
                         filter(workout_type__in=['Calisthenics', 'CrossFit']))

    for c_workout in filtered_workouts:
        result.append(
            f"{c_workout.name} from {c_workout.workout_type} type "
            f"has {c_workout.difficulty} difficulty!"
        )

    return "\n".join(result)


def get_high_difficulty_cardio_workouts():
    return Workout.objects.filter(workout_type='Cardio', difficulty='High').order_by('instructor')


def set_new_instructors():
    Workout.objects.filter(workout_type='Cardio').update(instructor='John Smith')
    Workout.objects.filter(workout_type='Strength').update(instructor='Michael Williams')
    Workout.objects.filter(workout_type='Yoga').update(instructor='Emily Johnson')
    Workout.objects.filter(workout_type='CrossFit').update(instructor='Sarah Davis')
    Workout.objects.filter(workout_type='Calisthenics').update(instructor='Chris Heria')


def set_new_duration_times():
    Workout.objects.filter(instructor='John Smith').update(duration='15 minutes')
    Workout.objects.filter(instructor='Sarah Davis').update(duration='30 minutes')
    Workout.objects.filter(instructor='Chris Heria').update(duration='45 minutes')
    Workout.objects.filter(instructor='Michael Williams').update(duration='1 hour')
    Workout.objects.filter(instructor='Emily Johnson').update(duration='1 hour and 30 minutes')


def delete_workouts():
    # Workout.objects.exclude(workout_type__in=['Strength', 'Calisthenics']).delete()
    Workout.objects.exclude(Q(workout_type='Strength') | Q(workout_type='Calisthenics')).delete()


# # Create two Workout instances
# workout1 = Workout.objects.create(
#     name="Push-Ups",
#     workout_type="Calisthenics",
#     duration="10 minutes",
#     difficulty="Intermediate",
#     calories_burned=200,
#     instructor="Chris Heria"
# )
#
# workout2 = Workout.objects.create(
#     name="Running",
#     workout_type="Cardio",
#     duration="30 minutes",
#     difficulty="High",
#     calories_burned=400,
#     instructor="John Smith"
# )
#
# # Run the functions
# print(show_workouts())
#
# high_difficulty_cardio_workouts = get_high_difficulty_cardio_workouts()
# for workout in high_difficulty_cardio_workouts:
#     print(f"{workout.name} by {workout.instructor}")
#
# set_new_instructors()
# workouts_with_new_instructors = Workout.objects.all()
# for workout in workouts_with_new_instructors:
#     print(f"Instructor: {workout.instructor}")
#
# set_new_duration_times()
# workouts_with_new_durations = Workout.objects.all()
# for workout in workouts_with_new_durations:
#     print(f"Duration: {workout.duration}")
#
# delete_workouts()
