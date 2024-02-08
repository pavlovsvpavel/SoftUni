from django.shortcuts import render, redirect
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import PetPhoto
from petstagram.common.forms import CommentForm


def add_photo(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
        "form": form,
    }

    return render(request, 'photos/photo-add-page.html', context)


def details_photo(request, pk):
    photo = PetPhoto.objects.get(pk=pk)
    likes = photo.photolike_set.all()
    comments = photo.comment_set.all()
    comment_form = CommentForm()

    context = {
        "photo": photo,
        "likes": likes,
        "comments": comments,
        "comment_form": comment_form,
    }

    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)

    if request.method == 'GET':
        form = PhotoEditForm(instance=pet_photo, initial=pet_photo.__dict__)

    else:
        form = PhotoEditForm(request.POST, instance=pet_photo)
        if form.is_valid():
            form.save()
            return redirect('photos_details', pk)

    context = {
        "form": form,
    }

    return render(request, 'photos/photo-edit-page.html', context)


def delete_photo(request, pk):
    photo = PetPhoto.objects.get(pk=pk)
    photo.delete()

    return redirect('home')
