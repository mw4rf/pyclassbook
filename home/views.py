from django.shortcuts import render
from django.conf import settings

def index(request):
    ''' App Home. '''
    # Stats
    from students.models import Student, Mark
    from courses.models import Course
    from exams.models import Exam, Subject
    counters = {}
    counters['students']    = Student.objects.count()
    counters['marks']       = Mark.objects.count()
    counters['courses']     = Course.objects.count()
    counters['exams']       = Exam.objects.count()
    counters['subjects']    = Subject.objects.count()
        
    # Build response
    response = {
        'APP_NAME': settings.APP_NAME,
        'APP_VERSION': settings.APP_VERSION,
        'COPYRIGHT': settings.COPYRIGHT,
        'counters': counters,
    }
    return render(request, 'home/index.html', response)