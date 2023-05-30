from django.shortcuts import render

def register_user(request):

    return render(request, 'account/register-page.html')


def login_user(request):

    return render(request, 'account/login-page.html')


def details_user(request, pk):

    return render(request, 'account/profile-details-page.html')


def edit_user(request, pk):

    return render(request, 'account/profile-edit-page.html')


def delete_user(request, pk):

    return render(request, 'account/profile-delete-page.html')