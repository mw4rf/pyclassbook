from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Exam, Subject

def index_full(request):
    ''' List of exams. '''
    exams = Exam.objects.order_by('date')
    context = {'exams': exams}
    return render(request, 'exams/index.html', context)

def index(request):
    exams_list = Exam.objects.order_by('date')
    paginator = Paginator(exams_list, 20) # Show 20 items per page
    page = request.GET.get('page')
    try:
        exams = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        exams = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        exams = paginator.page(paginator.num_pages)
    return render(request, 'exams/index.html', {"exams": exams})

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