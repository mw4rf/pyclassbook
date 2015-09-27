from django.shortcuts import render
from django.http import Http404

from .models import Student

def index(request):
    ''' List of students. '''
    students = Student.objects.order_by('created_at')
    context = {'students': students}
    return render(request, 'students/index.html', context)
    
def show(request, student_id):
    ''' Show a student details. '''
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        raise Http404("This student doesn't exist.")
    return render(request, 'students/show.html', {'student': student})
