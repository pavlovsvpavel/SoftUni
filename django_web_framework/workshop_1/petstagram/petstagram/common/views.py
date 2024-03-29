from django.shortcuts import render, redirect, resolve_url
from django.views import generic as views
from pyperclip import copy

from petstagram.common.models import PhotoLike
from petstagram.photos.models import PetPhoto
from petstagram.common.forms import CommentForm, SearchForm


# def index(request):
#     all_photos = PetPhoto.objects.all()
#     comment_form = CommentForm()
#     search_form = SearchForm(request.GET or None)
#
#     if search_form.is_valid():
#         all_photos = all_photos.filter(
#             pets__name__icontains=search_form.cleaned_data['pet_name']
#         )
#
#     context = {
#         'all_photos': all_photos,
#         'comment_form': comment_form,
#         'search_form': search_form,
#     }
#
#     return render(request, 'common/home-page.html', context)


class IndexView(views.ListView):
    queryset = PetPhoto.objects.all() \
        .prefetch_related("pets") \
        .prefetch_related("photolike_set")

    context_object_name = 'all_photos'
    template_name = 'common/home-page.html'
    comment_form = CommentForm()
    search_form = SearchForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['comment_form'] = self.comment_form
        context['search_form'] = self.search_form

        return context


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


def add_comment(request, pk):
    if request.method == "POST":
        photo = PetPhoto.objects.filter(pk=pk).first()
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.photo = photo
            comment.save()

    return redirect(request.META.get('HTTP_REFERER') + f"#{pk}")
