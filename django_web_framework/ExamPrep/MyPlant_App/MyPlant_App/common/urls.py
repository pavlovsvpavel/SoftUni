from django.urls import path

from MyPlant_App.common.views import IndexView, CatalogueView

urlpatterns = (
    path("", IndexView.as_view(), name="index"),
    path("catalogue/", CatalogueView.as_view(), name="catalogue"),
)
