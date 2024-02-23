from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("MyPlant_App.common.urls")),
    path("profile/", include("MyPlant_App.profiles.urls")),
    path("plant/", include("MyPlant_App.plants.urls")),
]
