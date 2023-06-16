from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('likes/<int:photo_pk>/', views.likes, name='likes'),
    path('share/<int:photo_pk>', views.link_for_share, name='share'),
]
