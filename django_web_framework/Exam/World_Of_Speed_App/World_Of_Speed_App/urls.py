from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("World_Of_Speed_App.common.urls")),
    path("car/", include("World_Of_Speed_App.cars.urls")),
    path("profile/", include("World_Of_Speed_App.profiles.urls"))
]
