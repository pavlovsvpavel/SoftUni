from django.contrib import admin

from main_app.models import Profile, Product, Order


def search_field_text(fields):
    result = []

    for field in fields:
        new_field = field.replace('_', ' ')
        result.append(new_field.capitalize())

    return f'Available searches by: {", ".join(result)}'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone_number', 'is_active']
    search_fields = ['full_name', 'email']
    search_help_text = search_field_text(search_fields)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'in_stock', 'is_available']
    list_filter = ['is_available']
    search_fields = ['name']
    search_help_text = search_field_text(search_fields)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['profile', 'total_price', 'creation_date', 'is_completed']
    list_filter = ['is_completed']
    search_fields = ['profile__full_name']
    search_help_text = search_field_text(search_fields)
