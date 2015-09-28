from django.shortcuts import render

def index(request):
    ''' App Home. '''
    return render(request, 'home/index.html')
