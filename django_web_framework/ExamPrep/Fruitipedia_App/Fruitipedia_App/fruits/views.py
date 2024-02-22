from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views import generic as views

from Fruitipedia_App.common.mixin import HideLabelsInFormsMixin, ShowPlaceholdersInFormsMixin
from Fruitipedia_App.fruits.mixins import FormFieldDisableViewMixin, RenameLabelsNamesInFormsMixin
from Fruitipedia_App.fruits.models import Fruit
from Fruitipedia_App.profiles.mixin import CheckForProfileMixin


class FruitCreateView(CheckForProfileMixin, HideLabelsInFormsMixin, ShowPlaceholdersInFormsMixin, views.CreateView):
    queryset = Fruit.objects.all()
    template_name = 'fruits/create-fruit.html'
    fields = ["name", "image_url", "description", "nutrition"]
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        form.instance.owner_id = self.get_profile().pk
        return super().form_valid(form)


class FruitDetailsView(CheckForProfileMixin, views.DetailView):
    queryset = Fruit.objects.all()
    template_name = "fruits/details-fruit.html"


class FruitEditView(CheckForProfileMixin, RenameLabelsNamesInFormsMixin, views.UpdateView):
    queryset = Fruit.objects.all()
    template_name = "fruits/edit-fruit.html"
    fields = ["name", "image_url", "description", "nutrition"]
    success_url = reverse_lazy("dashboard")


class FruitDeleteView(CheckForProfileMixin, FormFieldDisableViewMixin, RenameLabelsNamesInFormsMixin, views.DeleteView):
    queryset = Fruit.objects.all()
    template_name = "fruits/delete-fruit.html"
    success_url = reverse_lazy("dashboard")

    form_class = modelform_factory(
        Fruit, fields=("name", "image_url", "description")
    )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object

        return kwargs
