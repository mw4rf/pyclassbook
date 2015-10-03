from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .models import Course
from students.models import Student

@login_required
def index_full(request):
    ''' List of courses. '''
    # Sorting
    order_by = request.GET.get('order_by', 'start_date')
    # Requesting
    courses = Course.objects.all().order_by(order_by)
    context = {'courses': courses}
    return render(request, 'courses/index_full.html', context)

@login_required    
def index(request):
    # Sorting
    order_by = request.GET.get('order_by', 'start_date')
    # Requesting
    courses_list = Course.objects.all().order_by(order_by)
    # Paginating
    paginator = Paginator(courses_list, settings.COURSES_PER_PAGE) # config.py
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

@login_required    
def show(request, course_id):
    ''' Show a course details. '''
    try:
        course = Course.objects.get(pk=course_id)
        students = Student.objects.filter(courses__id=course_id)
    except Course.DoesNotExist:
        raise Http404("This course doesn't exist.")
    return render(request, 'courses/show.html', {'course': course, 'students': students})
