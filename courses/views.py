from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Course
from students.models import Student

def index_full(request):
    ''' List of courses. '''
    courses = Course.objects.order_by('created_at')
    context = {'courses': courses}
    return render(request, 'courses/index_full.html', context)
    
def index(request):
    courses_list = Course.objects.order_by('start_date')
    paginator = Paginator(courses_list, 20) # Show 20 items per page
    page = request.GET.get('page')
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        courses = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        courses = paginator.page(paginator.num_pages)
    return render(request, 'courses/index.html', {"courses": courses})
    
def show(request, course_id):
    ''' Show a course details. '''
    try:
        course = Course.objects.get(pk=course_id)
        students = Student.objects.filter(courses__id=course_id)
    except Course.DoesNotExist:
        raise Http404("This course doesn't exist.")
    return render(request, 'courses/show.html', {'course': course, 'students': students})
