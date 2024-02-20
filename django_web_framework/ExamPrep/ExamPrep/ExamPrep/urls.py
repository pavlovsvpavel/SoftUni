from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("ExamPrep.web.urls")),
    path("album/", include("ExamPrep.albums.urls")),
    path("profile/", include("ExamPrep.profiles.urls")),
]
