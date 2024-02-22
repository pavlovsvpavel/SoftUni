from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Fruitipedia_App.common.urls")),
    path("profile/", include("Fruitipedia_App.profiles.urls")),
    path("fruit/", include("Fruitipedia_App.fruits.urls"))
]
