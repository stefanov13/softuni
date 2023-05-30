from django.shortcuts import render

# def index(request):
    
#     return render(request, 'common/home-page.html')

def index(request):
    user = False

    context = {
        'user': user
    }

    return render(request, 'base/base.html', context)
