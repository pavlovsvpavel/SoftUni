from django.urls import path

from petstagram.common import views

urlpatterns = (
    path('', views.index, name='home'),
    path("like/<int:pk>/", views.like_functionality, name="like"),
    path("share/<int:pk>/", views.share_functionality, name="share"),
    path("comment/<int:pk>/", views.add_comment, name="comment"),
)
