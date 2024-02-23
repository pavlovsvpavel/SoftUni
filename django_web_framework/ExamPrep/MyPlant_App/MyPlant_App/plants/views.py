from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views import generic as views

from MyPlant_App.common.mixins import CheckForProfileMixin
from MyPlant_App.plants.mixin import FormFieldDisableViewMixin
from MyPlant_App.plants.models import Plant


class PlantCreateView(CheckForProfileMixin, views.CreateView):
    queryset = Plant.objects.all()
    template_name = 'plants/create-plant.html'
    success_url = reverse_lazy("catalogue")

    fields = ["plant_type", "name", "image_url", "description", "price"]

    def form_valid(self, form):
        form.instance.owner_id = self.get_profile().pk

        return super().form_valid(form)


class PlantDetailsView(CheckForProfileMixin, views.DetailView):
    queryset = Plant.objects.all()
    template_name = "plants/plant-details.html"


class PlantEditView(CheckForProfileMixin, views.UpdateView):
    queryset = Plant.objects.all()
    template_name = "plants/edit-plant.html"
    success_url = reverse_lazy("catalogue")

    fields = ("plant_type", "name", "image_url", "description", "price")


class PlantDeleteView(CheckForProfileMixin, FormFieldDisableViewMixin, views.DeleteView):
    queryset = Plant.objects.all()
    template_name = "plants/delete-plant.html"
    success_url = reverse_lazy("catalogue")

    form_class = modelform_factory(
        Plant, fields=("plant_type", "name", "image_url", "description", "price")
    )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object

        return kwargs
