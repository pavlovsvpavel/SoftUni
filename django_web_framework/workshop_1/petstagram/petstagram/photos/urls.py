from django.urls import path, include

from petstagram.photos import views
from petstagram.photos.views import PetPhotoAddView, PetPhotoDetailView, PetPhotoEditView, PetPhotoDeleteView

urlpatterns = (
    path('', include([
        path('add/', PetPhotoAddView.as_view(), name='add_photos'),
        path('<int:pk>/', PetPhotoDetailView.as_view(), name='photos_details'),
        path('<int:pk>/edit', PetPhotoEditView.as_view(), name='edit_photos'),
        path('<int:pk>/delete', PetPhotoDeleteView.as_view(), name='delete_photos')
    ])),
)
