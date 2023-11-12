import os
import django
from django.db.models import Count, Q, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Profile, Order, Product


# Problem 3
# print(Profile.objects.get_regular_customers())


# Problem 4
def get_profiles(search_string=None):
    if search_string is None:
        return ""

    query = (Q(full_name__icontains=search_string) |
             Q(email__icontains=search_string) |
             Q(phone_number__icontains=search_string))

    profiles = (Profile.objects.filter(query).
                annotate(orders_count=Count('profile_orders')).
                order_by('full_name'))

    result = []
    for profile in profiles:
        result.append(
            f"Profile: {profile.full_name}, "
            f"email: {profile.email}, "
            f"phone number: {profile.phone_number}, "
            f"orders: {profile.orders_count}"
        )

    return '\n'.join(result)


# print(get_profiles('Ma'))


def get_loyal_profiles():
    loyal_profiles = Profile.objects.get_regular_customers()

    if not loyal_profiles:
        return ""

    result = []
    for profile in loyal_profiles:
        result.append(
            f"Profile: {profile.full_name}, orders: {profile.orders_count}"
        )

    return '\n'.join(result)


# print(get_loyal_profiles())


def get_last_sold_products():
    latest_order = Order.objects.prefetch_related('products').last()

    if not latest_order:
        return ""

    products = latest_order.products.values('name').order_by('name')

    if not products:
        return ""

    result = []
    for product in products:
        result.append(product['name'])

    return f"Last sold products: {', '.join(result)}"


# print(get_last_sold_products())


# Problem 5
def get_top_products():
    products = (Product.objects.
                annotate(num_of_sales=Count('product_orders')).
                filter(num_of_sales__gt=0).
                order_by('-num_of_sales', 'name')[:5])

    if not products:
        return ""

    result = ["Top products:"]
    for product in products:
        result.append(
            f"{product.name}, sold {product.num_of_sales} times"
        )

    return '\n'.join(result)


# print(get_top_products())


def apply_discounts():
    orders = (Order.objects.
              annotate(num_of_products=Count('products')).
              filter(is_completed=False, num_of_products__gt=2).
              update(total_price=F('total_price') * 0.9))

    return f"Discount applied to {orders} orders."


# print(apply_discounts())


def complete_order():
    last_uncompleted_order = Order.objects.filter(is_completed=False).last()

    if not last_uncompleted_order:
        return ""

    last_uncompleted_order.is_completed = True
    last_uncompleted_order.save()

    for product in last_uncompleted_order.products.all():
        product.in_stock -= 1

        if product.in_stock <= 0:
            product.is_available = False

        product.save()

    return f"Order has been completed!"

# print(complete_order())
