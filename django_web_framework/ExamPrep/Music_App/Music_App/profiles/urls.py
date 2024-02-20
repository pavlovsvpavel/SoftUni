from django.urls import path

from Music_App.profiles.views import ProfileDetailsView, ProfileDeleteView

urlpatterns = (
    path("details/", ProfileDetailsView.as_view(), name="details_profile"),
    path("delete/", ProfileDeleteView.as_view(), name="delete_profile"),
)
