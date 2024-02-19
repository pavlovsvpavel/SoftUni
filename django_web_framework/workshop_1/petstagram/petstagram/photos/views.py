from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from petstagram.pets.models import Pet
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import PetPhoto
from petstagram.common.forms import CommentForm
from django.views import generic as views


# def add_photo(request):
#     form = PhotoCreateForm(request.POST or None, request.FILES or None)
#
#     if form.is_valid():
#         form.save()
#         return redirect('home')
#
#     context = {
#         "form": form,
#     }
#
#     return render(request, 'photos/photo-add-page.html', context)


class PetPhotoAddView(views.CreateView):
    queryset = PetPhoto.objects.all() \
        .prefetch_related('pets')
    form_class = PhotoCreateForm
    template_name = 'photos/photo-add-page.html'

    def get_success_url(self):
        return reverse('photos_details', kwargs={'pk': self.object.pk})


# def details_photo(request, pk):
#     photo = PetPhoto.objects.get(pk=pk)
#     likes = photo.photolike_set.all()
#     comments = photo.comments.all()
#     comment_form = CommentForm()
#
#     context = {
#         "photo": photo,
#         "likes": likes,
#         "comments": comments,
#         "comment_form": comment_form,
#     }
#
#     return render(request, 'photos/photo-details-page.html', context)


class PetPhotoDetailView(views.DetailView):
    queryset = PetPhoto.objects.all() \
        .prefetch_related("pets") \
        .prefetch_related("photolike_set") \
        .prefetch_related("comments")

    template_name = "photos/photo-details-page.html"
    comment_form = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['comment_form'] = self.comment_form

        return context


# def edit_photo(request, pk):
#     pet_photo = PetPhoto.objects.get(pk=pk)
#
#     if request.method == 'GET':
#         form = PhotoEditForm(instance=pet_photo, initial=pet_photo.__dict__)
#
#     else:
#         form = PhotoEditForm(request.POST, instance=pet_photo)
#         if form.is_valid():
#             form.save()
#             return redirect('photos_details', pk)
#
#     context = {
#         "form": form,
#     }
#
#     return render(request, 'photos/photo-edit-page.html', context)


class PetPhotoEditView(views.UpdateView):
    queryset = PetPhoto.objects.all() \
        .prefetch_related("pets")
    form_class = PhotoEditForm
    template_name = "photos/photo-edit-page.html"

    def get_success_url(self):
        return reverse('photos_details', kwargs={'pk': self.object.pk})


# def delete_photo(request, pk):
#     photo = PetPhoto.objects.get(pk=pk)
#     photo.delete()
#
#     return redirect('home')

# class PetPhotoDeleteView(views.DeleteView):
#     model = PetPhoto
#     success_url = reverse_lazy("index")
#
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#
#         self.object.remove(self.object)
#
#         return HttpResponseRedirect(self.get_success_url())


class PetPhotoDeleteView(views.DeleteView):
    # TODO: implement the logic
    pass
