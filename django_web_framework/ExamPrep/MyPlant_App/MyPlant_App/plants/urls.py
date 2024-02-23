from django.urls import path

from MyPlant_App.plants.views import PlantCreateView, PlantDetailsView, PlantEditView, PlantDeleteView

urlpatterns = (
    path("create/", PlantCreateView.as_view(), name="plant-create"),
    path("<int:pk>/details/", PlantDetailsView.as_view(), name="plant-details"),
    path("<int:pk>/edit/", PlantEditView.as_view(), name="plant-edit"),
    path("<int:pk>/delete/", PlantDeleteView.as_view(), name="plant-delete"),
)
