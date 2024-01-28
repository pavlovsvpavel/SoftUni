from django.contrib import admin
from petstagram.photos.models import PetPhoto


@admin.register(PetPhoto)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('updated_at', 'description', 'location', 'tagged_pets')

    @staticmethod
    def tagged_pets(obj):
        return ', '.join([p.name for p in obj.pets.all()])
