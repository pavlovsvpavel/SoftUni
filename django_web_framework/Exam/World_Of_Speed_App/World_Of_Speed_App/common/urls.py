from django.urls import path

from World_Of_Speed_App.common.views import IndexView

urlpatterns = (
    path("", IndexView.as_view(), name="index"),
)
