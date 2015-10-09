from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import ugettext as _

from courses.models import Course

import uuid
import statistics

class Student(models.Model):
    # UUID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Fields
    firstname   = models.CharField(max_length = 100, verbose_name=_('firstname'))
    lastname    = models.CharField(max_length = 100, verbose_name=_('lastname'))
    email       = models.EmailField(max_length = 254, blank=True, verbose_name=_('e-mail'))
    email_alt   = models.EmailField(max_length = 254, blank=True, verbose_name=_('Alternative e-mail'))
    birth       = models.DateField(null=True, blank=True, verbose_name=_('Birth date'))
    native_lang = models.BooleanField(default=True, verbose_name=_('Native language ?'))
    third_time  = models.BooleanField(default=False, verbose_name=_('Has a third time ?'))
    comments    = models.TextField(blank=True, default='', verbose_name=_('Comments'))
    # Auto
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    # Relations
    courses     = models.ManyToManyField(Course, verbose_name=_('Courses'))
    
    class Meta:
        verbose_name = _('Student')
    
    def __str__(self):
        return self.fullname()
    
    def fullname(self):
        return self.firstname + " " + self.lastname
    
    def marks(self):
        return Mark.objects.filter(student=self.id)
    
    def marks_for_course(self, course):
        marks = []
        for m in Mark.objects.filter(student=self.id):
            if m.subject.exam.course == course:
                marks.append(m)
        return marks
    
    def average(self):
        index = 0
        marks = 0
        for m in Mark.objects.filter(student=self.id).filter(count=True):
            for x in range(m.subject.exam.coeff):
                index = index + 1
                marks = marks + m.mark
        try:
            return float("{0:.2f}".format(marks / index))
        except ZeroDivisionError:
            return 0
    
    def average_for_course(self, course):
        index = 0
        marks = 0
        for m in Mark.objects.filter(student=self.id).filter(count=True):
            if m.subject.exam.course == course:
                for x in range(m.subject.exam.coeff):
                    marks = marks + m.mark
                    index = index + 1
        try:
            return float("{0:.2f}".format(marks / index))
        except ZeroDivisionError:
            return 0
    
    def stddev(self):
        marks = self.marks
        try:
            res = statistics.stdev(marks)
            return float("{0:.2f}".format(res)) # round to 2 decimal points
        except: #less than 2 marks : can't compute variance, exception thrown
            return 0
    
    def stddev_for_course(self, course):
        marks = self.marks_for_course(course)
        try:
            res = statistics.stdev(marks)
            return float("{0:.2f}".format(res)) # round to 2 decimal points
        except: #less than 2 marks : can't compute variance, exception thrown
            return 0

    @property
    def marks_progression(self):
        from django.utils import formats
        from collections import OrderedDict
        
        marks = Mark.objects.filter(student=self.id).filter(count=True).order_by('subject__exam__date')
        stats = OrderedDict() # needed to key the sort order by date, as simple dict do not preserve order
        for mark in marks:
            date = formats.date_format(mark.subject.exam.date, "SHORT_DATE_FORMAT")
            stats[date] = mark.mark
        return stats
        
    @property
    def average_progression(self):
        from django.utils import formats
        import statistics
        from collections import OrderedDict
        
        marks = Mark.objects.filter(student=self.id).filter(count=True).order_by('subject__exam__date')
        temp = []
        stats = OrderedDict() # needed to key the sort order by date, as simple dict do not preserve order
        for mark in marks:
            date = formats.date_format(mark.subject.exam.date, "SHORT_DATE_FORMAT")
            # Get average with this new mark
            for x in range(mark.subject.exam.coeff):
                temp.append(mark.mark)
            stats[date] = float("{0:.1f}".format(statistics.mean(temp)))
        return stats
        
    def future_average(self, course):
        marks = []
        for m in Mark.objects.filter(student=self.id).filter(count=True):
            if m.subject.exam.course == course:
                for x in range(m.subject.exam.coeff):
                    marks.append(m.mark)
        import statistics
        stats = {}
        for i in range(0,21):
            temp = marks[:] # temp is not a REFERENCE but a COPY of the original marks list
            temp.append(i)
            stats[i] = float("{0:.1f}".format(statistics.mean(temp)))
        return stats

    # Fields label in admin area (only for methods)
    fullname.short_description = "Name"
    
    # Fields sort order in admin area (only for methods)
    fullname.admin_order_field = 'lastname' # order by lastname
    

class Mark(models.Model):
    # UUID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Fields
    student     = models.ForeignKey(Student, verbose_name=_('Student'))
    subject     = models.ForeignKey('exams.Subject', verbose_name=_('Subject'))
    mark        = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], verbose_name=_('Mark'))
    count       = models.BooleanField(default=True, verbose_name=_('Count this in the average ?'))
    comment     = models.TextField(blank=True, verbose_name=_('Comments'))
    # Auto
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Mark')
    
    def __str__(self):
        return str(self.mark) + " - " + str(self.student)
        