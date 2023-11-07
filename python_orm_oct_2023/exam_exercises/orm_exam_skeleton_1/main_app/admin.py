from django.contrib import admin

from main_app.models import Director, Actor, Movie


def search_field_text(fields):
    result = []

    for field in fields:
        new_field = field.replace('_', ' ')
        result.append(new_field.capitalize())

    return f'Available searches by: {", ".join(result)}'


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'birth_date', 'nationality']
    list_filter = ['years_of_experience']
    search_fields = ['full_name', 'nationality']
    search_help_text = search_field_text(search_fields)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'birth_date', 'nationality']
    list_filter = ['is_awarded']
    search_fields = ['full_name']
    readonly_fields = ['last_updated']
    search_help_text = search_field_text(search_fields)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'storyline', 'rating', 'director']
    list_filter = ['is_awarded', 'is_classic', 'genre']
    search_fields = ['title', 'director__full_name']
    readonly_fields = ['last_updated']
    search_help_text = search_field_text(search_fields)
