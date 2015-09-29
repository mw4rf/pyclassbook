from django.shortcuts import render
from django.http import Http404

from .models import Exam, Subject

def index(request):
    ''' List of exams. '''
    exams = Exam.objects.order_by('course')
    context = {'exams': exams}
    return render(request, 'exams/index.html', context)
    
def exam(request, exam_id):
    ''' Show an exam details. '''
    try:
        exam = Exam.objects.get(pk=exam_id)
    except Exam.DoesNotExist:
        raise Http404("This exam doesn't exist.")
    return render(request, 'exams/show.html', {'exam': exam})

def subject(request, subject_id):
    ''' Show a subject details. '''
    try:
        subject = Subject.objects.get(pk=subject_id)
    except Exam.DoesNotExist:
        raise Http404("This subject doesn't exist.")
    return render(request, 'subjects/show.html', {'subject': subject})