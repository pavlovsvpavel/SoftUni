from django.urls import path, include
from petstagram.pets.views import PetCreateView, PetDetailsView, PetEditView, PetDeleteView

urlpatterns = (
    path('', include([
        path('add/', PetCreateView.as_view(), name='add_pets'),
        path('<str:username>/pet/<slug:pet_slug>/', PetDetailsView.as_view(), name='details_pets'),
        path('<str:username>/pet/<slug:pet_slug>/pets/', PetEditView.as_view(), name='edit_pets'),
        path('<str:username>/pet/<slug:pet_slug>/delete/', PetDeleteView.as_view(), name='delete_pets'),
    ])),
)