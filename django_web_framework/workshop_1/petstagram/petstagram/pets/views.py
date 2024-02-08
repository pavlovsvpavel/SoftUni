from django.shortcuts import render, redirect
from petstagram.pets.models import Pet
from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.common.forms import CommentForm


def add_pet(request):
    form = PetCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("details-profile", pk=1)

    context = {
        "form": form,
    }

    return render(request, 'pets/pet-add-page.html', context)


def details_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.pet_photos.all()
    comment_form = CommentForm()

    context = {
        "pet": pet,
        "all_photos": all_photos,
        "comment_form": comment_form,
    }

    return render(request, 'pets/pet-details-page.html', context)


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    if request.method == 'GET':
        form = PetEditForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect("details_pets", "username", pet_slug)

    context = {
        "pet": pet,
        "form": form,
    }

    return render(request, 'pets/pet-edit-page.html', context)


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    form = PetDeleteForm(instance=pet, initial=pet.__dict__)

    if request.method == 'POST':
        pet.delete()
        return redirect("details-profile", pk=1)

    context = {
        "pet": pet,
        "form": form,
    }

    return render(request, 'pets/pet-delete-page.html', context)
