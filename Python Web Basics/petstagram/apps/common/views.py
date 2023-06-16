from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from ..photos.models import Photo
from .models import Like

# def index(request):
    
#     return render(request, 'common/home-page.html')

def index(request):
    user = False

    all_photos = Photo.objects.all()

    context = {
        'user': user,
        'all_photos': all_photos,
    }

    return render(request, 'base/base.html', context)


def likes(request, photo_pk):
    photo = Photo.objects.get(pk=photo_pk)
    liked_object = Like.objects.filter(to_photo_id=photo_pk).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_pk}')


def link_for_share(request, photo_pk):
    copy(request.META['HTTP_HOST'] + resolve_url('photo-details', photo_pk))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_pk}')
