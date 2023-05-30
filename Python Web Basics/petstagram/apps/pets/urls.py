from django.urls import include, path
from . import views

urlpatterns = [
    path('add/', views.pets_add, name='pets-add'),
    path('<str:username>/pet/<slug:petname>/', include([
        path('', views.pets_details, name='pets-details'),
        path('edit/', views.pets_edit, name='pets-edit'),
        path('delete/', views.pets_delete, name='pets-delete'),
    ]))
]
