from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.photos_add, name='photos-add'),
    path('<int:pk>/', include([
        path('', views.photo_details, name='photo-details'),
        path('edit/', views.photo_edit, name='photo-edit'),
    ]))
]
