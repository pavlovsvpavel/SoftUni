from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Music_App.web.urls")),
    path("album/", include("Music_App.albums.urls")),
    path("profile/", include("Music_App.profiles.urls")),
]
