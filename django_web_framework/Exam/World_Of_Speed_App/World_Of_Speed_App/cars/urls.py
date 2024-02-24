from django.urls import path

from World_Of_Speed_App.cars.views import (
    CatalogueView, CarCreateView,
    CarDetailsView, CarEditView, CarDeleteView)

urlpatterns = (
    path("catalogue/", CatalogueView.as_view(), name="catalogue"),
    path("create", CarCreateView.as_view(), name="create_car"),
    path("<int:pk>/details/", CarDetailsView.as_view(), name="details_car"),
    path("<int:pk>/edit/", CarEditView.as_view(), name="edit_car"),
    path("<int:pk>/delete/", CarDeleteView.as_view(), name="delete_car"),
)
