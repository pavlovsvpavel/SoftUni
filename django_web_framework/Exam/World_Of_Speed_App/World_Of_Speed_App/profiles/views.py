from django.forms import PasswordInput
from django.urls import reverse_lazy
from django.views import generic as views

from World_Of_Speed_App.cars.mixins import CarsTotalPriceMixin
from World_Of_Speed_App.profiles.mixins import GetProfileMixin
from World_Of_Speed_App.profiles.models import Profile
from World_Of_Speed_App.cars.models import Car


class ProfileCreateView(views.CreateView):
    queryset = Profile.objects.all()
    template_name = "profiles/profile-create.html"
    success_url = reverse_lazy("catalogue")

    fields = ("username", "email", "age", "password")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['age'].help_text = "Age requirement: 21 years and above."

        form.fields['password'].widget = PasswordInput()
        return form


class ProfileDetailsView(GetProfileMixin, CarsTotalPriceMixin, views.DetailView):
    queryset = Profile.objects.all()
    template_name = "profiles/profile-details.html"

    def get_object(self, queryset=None):
        return self.get_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["cars"] = Car.objects.all()

        return context


class ProfileEditView(GetProfileMixin, views.UpdateView):
    queryset = Profile.objects.all()
    template_name = "profiles/profile-edit.html"
    success_url = reverse_lazy("details_profile")

    fields = "__all__"

    def get_object(self, queryset=None):
        return self.get_profile()


class ProfileDeleteView(GetProfileMixin, views.DeleteView):
    queryset = Profile.objects.all()
    template_name = "profiles/profile-delete.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return self.get_profile()
