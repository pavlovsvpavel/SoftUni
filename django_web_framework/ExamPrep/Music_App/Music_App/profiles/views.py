from django.urls import reverse_lazy
from django.views import generic as views
from Music_App.profiles.models import Profile
from Music_App.profiles.mixins import IsProfileMixin


class ProfileDetailsView(IsProfileMixin, views.DetailView):
    queryset = Profile.objects.all()
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        return self.get_profile()


class ProfileDeleteView(IsProfileMixin, views.DeleteView):
    queryset = Profile.objects.all()
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.get_profile()
