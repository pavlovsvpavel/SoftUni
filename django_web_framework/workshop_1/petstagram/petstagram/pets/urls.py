from django.urls import path, include

from petstagram.pets import views

urlpatterns = (
    path('pets/', include([
        path('add/', views.add_pets, name='add_pets'),
        path('<str:username>/pet/<slug:pet_slug>/', views.details_pets, name='details_pets'),
        path('<str:username>/pet/<slug:pet_slug>/pets/', views.edit_pets, name='edit_pets'),
        path('<str:username>/pet/<slug:pet_slug>/delete/', views.delete_pets, name='delete_pets'),
    ])),
)