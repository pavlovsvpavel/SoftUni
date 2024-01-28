from django.urls import path, include

from petstagram.photos import views

urlpatterns = (
    path('', include([
        path('add/', views.add_photos, name='add_photos'),
        path('<int:pk>/', views.details_photos, name='photos_details'),
        path('<int:pk>/edit', views.edit_photos, name='edit_photos')
    ])),
)
