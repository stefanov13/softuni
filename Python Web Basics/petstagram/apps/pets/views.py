from django.shortcuts import render

def pets_add(request):

    return render(request, 'pets/pet-add-page.html')


def pets_details(request, username, petname):

    return render(request, 'pets/pet-details-page.html')


def pets_edit(request, username, petname):

    return render(request, 'pets/pet-edit-page.html')


def pets_delete(request, username, petname):

    return render(request, 'pets/pet-delete-page.html')
