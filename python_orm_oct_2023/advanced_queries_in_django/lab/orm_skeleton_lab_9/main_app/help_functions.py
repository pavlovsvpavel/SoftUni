from django.db.models import Sum, Q, F

from main_app.models import Product, Order


def product_quantity_ordered():
    result = []

    product_orders = (Product.objects.filter(orderproduct__order_id__isnull=False).
                      annotate(total_ordered_quantity=Sum('orderproduct__quantity')).
                      order_by('-total_ordered_quantity'))

    for order in product_orders:
        result.append(f"Quantity ordered of {order.name}: {order.total_ordered_quantity}")

    return '\n'.join(result)


def ordered_products_per_customer():
    result = []

    ordered_products_by_customer = (
        Order.objects.prefetch_related('orderproduct_set__product__category').
        order_by('id')
    )

    for order in ordered_products_by_customer:
        result.append(f"Order ID: {order.id}, Customer: {order.customer.username}")

        for ordered_product in order.orderproduct_set.all():
            result.append(f"- Product: {ordered_product.product.name}, "
                          f"Category: {ordered_product.product.category.name}")

    return '\n'.join(result)


def filter_products():
    result = []

    query = Q(price__gt=3.00) & Q(is_available=True)

    filtered_products = (
        Product.objects.filter(query).order_by('-price', 'name')
    )

    for product in filtered_products:
        result.append(f"{product.name}: {product.price}lv.")

    return '\n'.join(result)


def give_discount():
    result = []

    discounted_price = F('price') * 0.7
    query = Q(is_available=True) & Q(price__gt=3.00)
    Product.objects.filter(query).update(price=discounted_price)

    all_products = (
        Product.objects.filter(is_available=True).order_by('-price', 'name')

    )

    for product in all_products:
        result.append(f"{product.name}: {product.price}lv.")

    return '\n'.join(result)
