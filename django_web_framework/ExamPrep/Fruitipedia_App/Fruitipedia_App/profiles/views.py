from django.forms import PasswordInput
from django.urls import reverse_lazy
from django.views import generic as views

from Fruitipedia_App.common.mixin import HideLabelsInFormsMixin, ShowPlaceholdersInFormsMixin
from Fruitipedia_App.fruits.models import Fruit
from Fruitipedia_App.profiles.mixin import CheckForProfileMixin
from Fruitipedia_App.profiles.models import Profile


class ProfileCreateView(HideLabelsInFormsMixin, ShowPlaceholdersInFormsMixin, views.CreateView):
    queryset = Profile.objects.all()
    template_name = 'profiles/create-profile.html'
    fields = ['first_name', 'last_name', 'email', 'password']
    success_url = reverse_lazy("dashboard")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['password'].help_text = "*Password length requirements: 8 to 20 characters"

        form.fields['password'].widget = PasswordInput()
        return form


class ProfileDetailsView(CheckForProfileMixin, views.DetailView):
    queryset = Profile.objects.all()
    template_name = 'profiles/details-profile.html'

    def get_object(self, queryset=None):
        return self.get_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["fruits"] = Fruit.objects.all()

        return context


class ProfileUpdateView(CheckForProfileMixin, views.UpdateView):
    queryset = Profile.objects.all()
    template_name = "profiles/edit-profile.html"
    fields = ['first_name', 'last_name', 'image_url', 'age']
    success_url = reverse_lazy("profile_details")

    def get_object(self, queryset=None):
        return self.get_profile()


class ProfileDeleteView(CheckForProfileMixin, views.DeleteView):
    queryset = Profile.objects.all()
    template_name = "profiles/delete-profile.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return self.get_profile()
