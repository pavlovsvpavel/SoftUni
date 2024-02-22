from django.urls import path

from Fruitipedia_App.fruits.views import FruitCreateView, FruitDetailsView, FruitEditView, FruitDeleteView

urlpatterns = (
    path("create/", FruitCreateView.as_view(), name="fruit_create"),
    path("<int:pk>/details/", FruitDetailsView.as_view(), name="fruit_details"),
    path("<int:pk>/edit/", FruitEditView.as_view(), name="fruit_edit"),
    path("<int:pk>/delete/", FruitDeleteView.as_view(), name="fruit_delete"),
)
