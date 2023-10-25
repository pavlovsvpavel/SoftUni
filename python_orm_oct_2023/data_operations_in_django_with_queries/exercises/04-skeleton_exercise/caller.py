import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom


def create_pet(name: str, species: str):
    Pet.objects.create(
        name=name,
        species=species
    )

    return f"{name} is a very cute {species}!"


# print(create_pet('Buddy', 'Dog'))
# print(create_pet('Whiskers', 'Cat'))
# print(create_pet('Rocky', 'Hamster'))


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )

    return f"The artifact {name} is {age} years old!"


def delete_all_artifacts():
    Artifact.objects.all().delete()


# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500,
#                       'A legendary sword with a rich history', True))
# print(create_artifact('Crystal Amulet', 'Mystic Forest', 300,
#                       'A magical amulet believed to bring good fortune', True))
# delete_all_artifacts()


# def create_locations():
#     LOCATIONS = [
#         {
#             'name': 'Sofia',
#             'region': 'Sofia Region',
#             'population': 1329000,
#             'description': 'The capital of Bulgaria and the largest city in the country',
#             'is_capital': False
#         },
#         {
#             'name': 'Plovdiv',
#             'region': 'Plovdiv Region',
#             'population': 346942,
#             'description': 'The second-largest city in Bulgaria with a rich historical heritage',
#             'is_capital': False
#         },
#         {
#             'name': 'Varna',
#             'region': 'Varna Region',
#             'population': 330486,
#             'description': 'A city known for its sea breeze and beautiful beaches on the Black Sea',
#             'is_capital': False
#         }
#     ]
#
#     for c_location in LOCATIONS:
#         Location.objects.create(**c_location)


def show_all_locations():
    locations_info = []

    for c_location in Location.objects.all().order_by('-id'):
        locations_info.append(
            f"{c_location.name} has a population of {c_location.population}!"
        )

    return "\n".join(locations_info)


def new_capital():
    first_location = Location.objects.first()
    if first_location:
        first_location.is_capital = True
        first_location.save()


def get_capitals():
    capital = Location.objects.values('name').filter(is_capital=True)

    return capital


def delete_first_location():
    first_location = Location.objects.first()
    if first_location:
        first_location.delete()


# create_locations()
# print(show_all_locations())
# print(new_capital())
# print(get_capitals())
# delete_first_location()


# def create_cars():
#     CARS = [
#         {
#             'model': 'Mercedes C63 AMG',
#             'year': 2019,
#             'color': 'white',
#             'price': 120000.00
#         },
#         {
#             'model': 'Audi Q7 S line',
#             'year': 2023,
#             'color': 'black',
#             'price': 183900.00
#         },
#         {
#             'model': 'Chevrolet Corvette',
#             'year': 2021,
#             'color': 'dark grey',
#             'price': 199999.00
#         }
#     ]
#
#     for c_car in CARS:
#         Car.objects.create(**c_car)


def apply_discount():
    for c_car in Car.objects.all():
        current_discount = sum(int(x) for x in str(c_car.year) if x.isdigit()) / 100
        c_car.price_with_discount = float(c_car.price) - (float(c_car.price) * current_discount)
        c_car.save()


def get_recent_cars():
    cars = Car.objects.values('model', 'price_with_discount').filter(year__gt=2020)

    return cars


def delete_last_car():
    last_car = Car.objects.last()
    if last_car:
        last_car.delete()


# create_cars()
# apply_discount()
# print(get_recent_cars())
# delete_last_car()


# def create_tasks():
#     Task.objects.create(
#         title='Simple Task',
#         description='This is a sample task description',
#         due_date='2023-10-31',
#         is_finished=False
#     )


def show_unfinished_tasks():
    tasks = []

    for c_task in Task.objects.all():
        tasks.append(
            f"Task - {c_task.title} needs to be done until {c_task.due_date}!"
        )

    return "\n".join(tasks)


def complete_odd_tasks():
    for c_task in Task.objects.all():
        if c_task.id % 2 != 0:
            c_task.is_finished = True
            c_task.save()


def encode_and_replace(text: str, task_title: str):
    encoded_string = ""
    for el in text:
        encoded_string += chr(ord(el) - 3)

    for c_task in Task.objects.all():
        if c_task.title == task_title:
            c_task.description = encoded_string
            c_task.save()


# create_tasks()
# print(show_unfinished_tasks())
# complete_odd_tasks())
# encode_and_replace("Zdvk#wkh#glvkhv$", "Simple Task")
# print(Task.objects.get(title='Simple Task').description)


def create_rooms():
    ROOMS = [
        {
            'room_number': 101,
            'room_type': 'Standard',
            'capacity': 2,
            'amenities': 'Tv',
            'price_per_night': 100.00
        },
        {
            'room_number': 201,
            'room_type': 'Deluxe',
            'capacity': 3,
            'amenities': 'Wi-Fi',
            'price_per_night': 200.00
        },
        {
            'room_number': 501,
            'room_type': 'Standard',
            'capacity': 6,
            'amenities': 'Jacuzzi',
            'price_per_night': 400.00
        }
    ]

    for room in ROOMS:
        HotelRoom.objects.create(**room)


def get_deluxe_rooms():
    info = []
    # even_ids = HotelRoom.objects.annotate(odd=F('id') % 2).filter(odd=False)
    for room in HotelRoom.objects.all().filter(room_type='Deluxe'):

        if room.id % 2 == 0:
            info.append(
                f"Deluxe room with number {room.room_number} "
                f"costs {room.price_per_night}$ per night!"
            )

    return "\n".join(info)


def increase_room_capacity():
    rooms = HotelRoom.objects.all().order_by('id')

    for idx, c_room in enumerate(rooms):
        if not c_room.is_reserved:
            continue

        if idx == 0:
            c_room.capacity += c_room.id

        else:
            c_room.capacity += rooms[idx - 1].capacity

        c_room.save()


def reserve_first_room():
    first_room = HotelRoom.objects.first()

    if first_room:
        first_room.is_reserved = True
        first_room.save()


def delete_last_room():
    last_room = HotelRoom.objects.last()
    if last_room:
        last_room.delete()


# create_rooms()
# print(get_deluxe_rooms())
# increase_room_capacity()
# reserve_first_room()
# print(HotelRoom.objects.get(room_number=101).is_reserved)
# delete_last_room()
