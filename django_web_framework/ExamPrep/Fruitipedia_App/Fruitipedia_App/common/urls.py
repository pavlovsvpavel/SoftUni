from django.urls import path

from Fruitipedia_App.common.views import IndexView, DashboardView

urlpatterns = (
    path("", IndexView.as_view(), name="index"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
)
