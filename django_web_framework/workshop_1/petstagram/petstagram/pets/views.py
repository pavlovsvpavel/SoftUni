from django.shortcuts import render


# Create your views here.
def add_pets(request):
    return render(request, 'pets/pet-add-page.html')


def details_pets(request):
    return render(request, 'pets/pet-details-page.html')


def edit_pets(request):
    return render(request, 'pets/pet-edit-page.html')


def delete_pets(request):
    return render(request, 'pets/pet-delete-page.html')
