from django.urls import path, include

from petstagram.photos import views

urlpatterns = (
    path('', include([
        path('add/', views.add_photo, name='add_photos'),
        path('<int:pk>/', views.details_photo, name='photos_details'),
        path('<int:pk>/edit', views.edit_photo, name='edit_photos'),
        path('<int:pk>/delete', views.delete_photo, name='delete_photos')
    ])),
)
