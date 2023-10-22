import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Person, Item, Smartphone, Order


def add_products():
    product1 = Person(
        name='Ivan',
        age=25
    )
    product1.save()

    product2 = Person(
        name='Pesho',
        age=12
    )
    product2.save()
    return 'Products added successfully'


def add_items():
    item1 = Item(
        name='Joto',
        price=25,
        quantity=1000
    )
    item1.save()

    item2 = Item(
        name='JJJ',
        price=100,
        quantity=100
    )
    item2.save()
    return 'Items added successfully'


def add_smartphones():
    item1 = Smartphone(
        brand='Samsung',
        price=1000
    )
    item1.save()

    item2 = Smartphone(
        brand='iPhone',
        price=2000
    )
    item2.save()
    return 'Smartphones added successfully'


def add_orders():
    order1 = Order(
        product_name='Watch',
        customer_name='Ivan',
        order_date='2023-10-10',
        status='Pending',
        product_price=100,
        total_price=100
    )
    order1.save()

    order2 = Order(
        product_name='Phone',
        customer_name='Pesho',
        order_date='2023-10-22',
        status='Completed',
        product_price=1000,
        total_price=1000
    )
    order2.save()

    order3 = Order(
        product_name='TV',
        customer_name='Gosho',
        order_date='2023-10-20',
        status='Cancelled',
        product_price=500,
        total_price=500
    )
    order3.save()

    return 'Order added successfully'


# print(add_products())
# print(add_items())
# print(add_smartphones())
# print(add_orders())

