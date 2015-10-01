from django.db import models
from django.utils.translation import ugettext as _
import uuid

class Course(models.Model):
    # UUID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Fields
    name =          models.CharField(max_length = 254, verbose_name=_('Name'))
    level =         models.CharField(max_length=10, blank=True, verbose_name=_('Level'))
    place =         models.CharField(max_length = 254, blank=True, verbose_name=_('Place'))
    kind =          models.CharField(max_length = 254, blank=True, verbose_name=_('Kind'))
    comments =      models.TextField(blank=True, verbose_name=_('Comments'))
    start_date =    models.DateField(blank=True, verbose_name=_('Start date'))
    end_date =      models.DateField(blank=True, verbose_name=_('End date'))
    # Auto
    created_at =    models.DateTimeField(auto_now_add=True)
    updated_at =    models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Course')
    
    def __str__(self):
        return self.name
    
    @property
    def fullname(self):
        return "%s, %s, %s-%s" % (self.name, self.place, self.start_date.year, self.end_date.year)
    
    @property
    def exams(self):
        from exams.models import Exam
        return Exam.objects.all().filter(course=self.id)
    
    @property
    def students(self):
        from students.models import Student
        students = Student.objects.all().filter(courses__id=self.id)
        return students
        
    @property
    def averages(self):
        ''' Returns a list of averages for this course. '''
        students = self.students
        averages = [student.average_for_course(self) for student in students]
        return averages
        
    @property
    def count_averages_occurrences(self):
        ''' Returns an array with with the number of occurrences for each student's average mark.
        e.g. {0: 3, 1: 0, 2: 0, 3: 0, 4: 2, 5: 0, ... } : 3 students have 0/20, 2 students have 4/20
        '''
        averages = self.averages
        count = [x for x in range(0,21)]
        stats = {}
        for x in count:
            stats[x] = averages.count(x)
        return stats
        

