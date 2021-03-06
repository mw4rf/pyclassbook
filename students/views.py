from django.shortcuts import render

from django.http import Http404
from django.http import HttpResponse

from django.conf import settings

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.decorators import login_required

from .models import Student, Mark
from exams.models import Subject

from .forms import MarkForm

@login_required
def index_full(request):
    ''' List of students. '''
    # Sorting
    order_by = request.GET.get('order_by', 'lastname')
    # Requesting
    students = Student.objects.all().order_by(order_by)
    context = {'students': students}
    return render(request, 'students/index_full.html', context)

@login_required
def index(request):
    # Sorting
    order_by = request.GET.get('order_by', 'lastname')
    # Requesting
    students_list = Student.objects.all().order_by(order_by)
    # Paginating
    paginator = Paginator(students_list, settings.STUDENTS_PER_PAGE) # config.py
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
        # Add Mark Form
        if request.method == 'POST':
            form = MarkForm(request.POST)
            if form.is_valid():
                markn = form.cleaned_data['mark']
                subject = form.cleaned_data['subject']
                count = form.cleaned_data['count']
                comment = form.cleaned_data['comment']
                
                mark = Mark.objects.create(mark=markn, subject=subject, count=count, comment=comment, student=student)
                mark.save()
                student.save()
    except Student.DoesNotExist:
        raise Http404("This student doesn't exist.")
    # Reset form
    form = MarkForm()
    return render(request, 'students/show.html', {'student': student, 'form': form})

@login_required
def csv(request):
    import csv
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    writer = csv.writer(response)
    
    fields = Student._meta.fields # get fields names
    students = Student.objects.all().order_by('-created_at')
    
    # Output headers
    headers = []
    for field in fields:
        headers.append(field.name)
    writer.writerow(headers)
    
    # Output fields
    for student in students:
           row = []
           for field in fields:
                row.append(str(getattr(student, field.name)))
           writer.writerow(row)

    return response
    
    
## Forms
@login_required
def add_mark(request, student_id):
    if request.method == 'POST':
        form = MarkForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            pass

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MarkForm()

    return render(request, 'students/show.html', {'student': student, 'form': form})
