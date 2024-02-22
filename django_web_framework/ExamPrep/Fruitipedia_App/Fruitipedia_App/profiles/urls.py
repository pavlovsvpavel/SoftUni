from django.urls import path

from Fruitipedia_App.profiles.views import ProfileCreateView, ProfileDetailsView, ProfileUpdateView, ProfileDeleteView

urlpatterns = (
    path("create/", ProfileCreateView.as_view(), name="profile_create"),
    path("details/", ProfileDetailsView.as_view(), name="profile_details"),
    path("edit/", ProfileUpdateView.as_view(), name="profile_edit"),
    path("delete/", ProfileDeleteView.as_view(), name="profile_delete"),
)
