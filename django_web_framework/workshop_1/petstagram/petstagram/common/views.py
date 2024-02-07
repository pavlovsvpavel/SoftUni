from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram.common.models import PhotoLike
from petstagram.photos.models import PetPhoto


def index(request):
    all_photos = PetPhoto.objects.all()

    context = {
        'all_photos': all_photos,
    }

    return render(request, 'common/home-page.html', context)


def like_functionality(request, pk):
    photo_like = PhotoLike.objects.filter(photo_id=pk).first()

    if photo_like:
        photo_like.delete()
    else:
        PhotoLike.objects.create(photo_id=pk)

    return redirect(request.META.get('HTTP_REFERER') + f"#{pk}")


def share_functionality(request, pk):
    copy(request.META["HTTP_HOST"] + resolve_url("photos_details", pk))

    return redirect(request.META.get('HTTP_REFERER') + f"#{pk}")
