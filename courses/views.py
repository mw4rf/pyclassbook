from django.shortcuts import render

from .models import Course

def index(request):
    ''' List of courses. '''
    courses = Course.objects.order_by('created_at')
    context = {'courses': courses}
    return render(request, 'courses/index.html', context)
    
def show(request, course_id):
    ''' Show a course details. '''
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        raise Http404("This course doesn't exist.")
    return render(request, 'courses/show.html', {'course': course})
