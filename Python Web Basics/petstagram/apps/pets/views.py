from django.shortcuts import render

from ..photos.models import Photo
from .models import Pet

def pets_add(request):

    return render(request, 'pets/pet-add-page.html')


def pets_details(request, username, petname):
    pet = Pet.objects.get(slug=petname)
    all_photos = Photo.objects.all()

    context = {
        'pet': pet,
        'all_photos': all_photos,
        
    }

    return render(request, 'pets/pet-details-page.html', context)


def pets_edit(request, username, petname):

    return render(request, 'pets/pet-edit-page.html')


def pets_delete(request, username, petname):

    return render(request, 'pets/pet-delete-page.html')
