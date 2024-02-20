from django.urls import path

from Music_App.web.views import IndexView

urlpatterns = (
    path("", IndexView.as_view(), name="index"),
)
