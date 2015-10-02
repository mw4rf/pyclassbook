from django.shortcuts import render
from django.conf import settings

def index(request):
    ''' App Home. '''
    response = {
        'APP_NAME': settings.APP_NAME,
        'APP_VERSION': settings.APP_VERSION,
        'COPYRIGHT': settings.COPYRIGHT
    }
    return render(request, 'home/index.html', response)