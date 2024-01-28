from django.urls import path, include

from petstagram.accounts import views

urlpatterns = (
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/<int:pk>/', include([
        path('', views.details_profile, name='details-profile'),
        path('edit/', views.edit_profile, name='profile-edit'),
        path('delete/', views.delete_profile, name='delete-profile')
    ])),
)
