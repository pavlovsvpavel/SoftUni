from django.urls import reverse_lazy
from django.views import generic as views

from MyPlant_App.common.mixins import CheckForProfileMixin
from MyPlant_App.plants.models import Plant
from MyPlant_App.profiles.models import Profile


class ProfileCreateView(views.CreateView):
    queryset = Profile.objects.all()
    template_name = "profiles/create-profile.html"
    success_url = reverse_lazy("catalogue")

    fields = ["username", "first_name", "last_name"]


class ProfileDetailsView(CheckForProfileMixin, views.DetailView):
    queryset = Profile.objects.all()
    template_name = "profiles/profile-details.html"

    def get_object(self, queryset=None):
        return self.get_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["plants"] = Plant.objects.all()

        return context


class ProfileEditView(CheckForProfileMixin, views.UpdateView):
    queryset = Profile.objects.all()
    template_name = "profiles/edit-profile.html"
    success_url = reverse_lazy("profile_details")

    fields = ["username", "first_name", "last_name", "profile_picture"]

    def get_object(self, queryset=None):
        return self.get_profile()


class ProfileDeleteView(CheckForProfileMixin, views.DeleteView):
    queryset = Profile.objects.all()
    template_name = "profiles/delete-profile.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return self.get_profile()






