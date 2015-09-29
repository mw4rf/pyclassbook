from django.db import models
from datetime import date
from django.utils.translation import ugettext as _

import uuid
import statistics

from students.models import Mark

class Exam(models.Model):
    # UUID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Fields
    name =          models.CharField(max_length = 254, default='', verbose_name=_('Name'))
    course =        models.ForeignKey('courses.Course', verbose_name=_('Course'))
    date =          models.DateField(blank=True, null=True, verbose_name=_('Date'))
    time_allowed =  models.IntegerField(blank=True, null=True, verbose_name=_('Time Allowed'))
    place =         models.CharField(max_length = 254, default='', verbose_name=_('Place'))
    comments =      models.TextField(blank=True, default='', verbose_name=_('Comments'))
    # Auto
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Exam')
        
    def __str__(self):
        return self.name + " (" + str(self.course) + ")"
    
    @property    
    def subjects(self):
        return Subject.objects.filter(exam=self.id)
    
    @property    
    def marks(self):
        return Mark.objects.filter(subject__in=self.subjects)
    
    @property
    def count_marks(self):
        return len(self.marks)
    
    @property
    def marks_as_array(self):
        marks = []
        for m in self.marks:
            marks.append(m.mark)
        return marks
     
    @property
    def average(self):
        try:
            res = statistics.mean(self.marks_as_array)
            return float("{0:.2f}".format(res)) # round to 2 decimal points
        except: #less than 2 marks : can't compute, exception thrown
            return 0
    
    @property
    def stddev(self):
        try:
            res = statistics.stdev(self.marks_as_array)
            return float("{0:.2f}".format(res)) # round to 2 decimal points
        except: #less than 2 marks : can't compute variance, exception thrown
            return 0
            
    @property
    def higher_mark(self):
        try:
            return max(self.marks_as_array)
        except:
            return 0
            
    @property
    def lower_mark(self):
        try:
            return min(self.marks_as_array)
        except:
            return 0
            
    @property
    def median(self):
        try:
            return statistics.median(self.marks_as_array)
        except:
            return 0
            
    @property
    def variance(self):
        try:
            res = statistics.variance(self.marks_as_array)
            return float("{0:.2f}".format(res)) # round to 2 decimal points
        except:
            return 0
    
class Subject(models.Model):
    # UUID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Fields
    exam =      models.ForeignKey(Exam, verbose_name=_('Exam'))
    title =     models.TextField(blank=True, default='', verbose_name=_('Title'))
    kind =      models.CharField(max_length = 254, default='', verbose_name=_('Kind'))
    # Auto
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Subject')
    
    def __str__(self):
        return str(self.exam) + "(" + self.kind + ")"
        
    @property
    def marks(self):
        return Mark.objects.filter(subject=self.id)
    
