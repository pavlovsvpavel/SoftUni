from django.shortcuts import render
from petstagram.pets.models import Pet


def add_pet(request):
    return render(request, 'pets/pet-add-page.html')


def details_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.pet_photos.all()

    context = {
        "pet": pet,
        "all_photos": all_photos,
    }

    return render(request, 'pets/pet-details-page.html', context)


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    context = {
        "pet": pet,
    }

    return render(request, 'pets/pet-edit-page.html', context)


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    context = {
        "pet": pet,
    }

    return render(request, 'pets/pet-delete-page.html', context)
