from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from petstagram.pets.models import Pet
from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.common.forms import CommentForm
from django.views import generic as views


# def add_pet(request):
#     form = PetCreateForm(request.POST or None)
#
#     if form.is_valid():
#         form.save()
#         return redirect("details-profile", pk=1)
#
#     context = {
#         "form": form,
#     }
#
#     return render(request, 'pets/pet-add-page.html', context)


class PetCreateView(views.CreateView):
    queryset = Pet.objects.all()
    form_class = PetCreateForm
    template_name = 'pets/pet-add-page.html'

    def get_success_url(self):
        return reverse("details-profile", kwargs={"pk": 1})


# def details_pet(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#     all_photos = pet.pet_photos.all()
#     comment_form = CommentForm()
#
#     context = {
#         "pet": pet,
#         "all_photos": all_photos,
#         "comment_form": comment_form,
#     }
#
#     return render(request, 'pets/pet-details-page.html', context)


class PetDetailsView(views.DetailView):
    queryset = Pet.objects.all() \
        .prefetch_related('pet_photos') \
        .prefetch_related('pet_photos__comments')

    template_name = 'pets/pet-details-page.html'

    slug_url_kwarg = 'pet_slug'

# def edit_pet(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#
#     if request.method == 'GET':
#         form = PetEditForm(instance=pet, initial=pet.__dict__)
#     else:
#         form = PetEditForm(request.POST, instance=pet)
#         if form.is_valid():
#             form.save()
#             return redirect("details_pets", "username", pet_slug)
#
#     context = {
#         "pet": pet,
#         "form": form,
#     }
#
#     return render(request, 'pets/pet-edit-page.html', context)


class PetEditView(views.UpdateView):
    queryset = Pet.objects.all()
    form_class = PetEditForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_success_url(self):
        return reverse("details-profile", kwargs={"pk": 1})


# def delete_pet(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#     form = PetDeleteForm(instance=pet, initial=pet.__dict__)
#
#     if request.method == 'POST':
#         pet.delete()
#         return redirect("details-profile", pk=1)
#
#     context = {
#         "pet": pet,
#         "form": form,
#     }
#
#     return render(request, 'pets/pet-delete-page.html', context)

class PetDeleteView(views.DeleteView):
    queryset = Pet.objects.all()
    form_class = PetDeleteForm
    template_name = 'pets/pet-delete-page.html'
    slug_url_kwarg = 'pet_slug'
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs
