from django.urls import path, include

from petstagram.pets import views

urlpatterns = (
    path('', include([
        path('add/', views.add_pet, name='add_pets'),
        path('<str:username>/pet/<slug:pet_slug>/', views.details_pet, name='details_pets'),
        path('<str:username>/pet/<slug:pet_slug>/pets/', views.edit_pet, name='edit_pets'),
        path('<str:username>/pet/<slug:pet_slug>/delete/', views.delete_pet, name='delete_pets'),
    ])),
)