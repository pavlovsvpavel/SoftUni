from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views import generic as views

from World_Of_Speed_App.cars.mixins import FormFieldDisableViewMixin
from World_Of_Speed_App.cars.models import Car
from World_Of_Speed_App.profiles.mixins import GetProfileMixin


class CatalogueView(GetProfileMixin, views.TemplateView):
    template_name = "cars/catalogue.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["cars"] = Car.objects.all()

        return context


class CarCreateView(GetProfileMixin, views.CreateView):
    queryset = Car.objects.all()
    template_name = "cars/car-create.html"
    success_url = reverse_lazy("catalogue")

    fields = ("type", "model", "year", "image_url", "price")

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields["image_url"].widget.attrs["placeholder"] = "https://..."

        return form

    def form_valid(self, form):
        form.instance.owner_id = self.get_profile().pk

        return super().form_valid(form)


class CarDetailsView(GetProfileMixin, views.DetailView):
    queryset = Car.objects.all()
    template_name = "cars/car-details.html"


class CarEditView(GetProfileMixin, views.UpdateView):
    queryset = Car.objects.all()
    template_name = "cars/car-edit.html"
    success_url = reverse_lazy("catalogue")

    fields = ("type", "model", "year", "image_url", "price")


class CarDeleteView(GetProfileMixin, FormFieldDisableViewMixin, views.DeleteView):
    queryset = Car.objects.all()
    template_name = "cars/car-delete.html"
    success_url = reverse_lazy("catalogue")

    form_class = modelform_factory(
        Car, fields=("type", "model", "year", "image_url", "price")
    )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object

        return kwargs
