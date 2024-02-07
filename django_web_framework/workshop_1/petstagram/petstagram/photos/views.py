from django.shortcuts import render
from petstagram.photos.models import PetPhoto


def add_photo(request):
    return render(request, 'photos/photo-add-page.html')


def details_photo(request, pk):
    photo = PetPhoto.objects.get(pk=pk)
    likes = photo.photolike_set.all()
    comments = photo.comment_set.all()

    context = {
        "photo": photo,
        "likes": likes,
        "comments": comments,
    }

    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request, pk):
    context = {

    }

    return render(request, 'photos/photo-edit-page.html', context)
