from django.shortcuts import render
from . import models

def photos_add(request):

    return render(request, 'photos/photo-add-page.html')


def photo_details(request, pk):
    picture = models.Photo.objects.filter(pk=pk).get()
    pic_comments = picture.comment_set.all()

    context = {
        "pic_comments": pic_comments,
        "picture": picture,
    }
    return render(request, 'photos/photo-details-page.html', context=context)


def photo_edit(request, pk):

    return render(request, 'photos/photo-edit-page.html')
