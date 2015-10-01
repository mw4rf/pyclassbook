from django.shortcuts import render
from django.http import Http404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from .models import Student

@login_required
def index_full(request):
    ''' List of students. '''
    students = Student.objects.order_by('created_at')
    context = {'students': students}
    return render(request, 'students/index_full.html', context)

@login_required
def index(request):
    # Sorting
    order_by = request.GET.get('order_by', 'lastname')
    # Requesting
    students_list = Student.objects.all().order_by(order_by)
    # Paginating
    paginator = Paginator(students_list, 100) # Show 100 items per page
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        students = paginator.page(paginator.num_pages)
    return render(request, 'students/index.html', {"students": students})

@login_required
def show(request, student_id):
    ''' Show a student details. '''
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        raise Http404("This student doesn't exist.")
    return render(request, 'students/show.html', {'student': student})
