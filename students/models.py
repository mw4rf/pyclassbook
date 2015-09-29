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
    email       = models.EmailField(max_length = 254, verbose_name=_('e-mail'))
    email_alt   = models.EmailField(max_length = 254, blank=True, verbose_name=_('Alternative e-mail'))
    birth       = models.DateField(null=True, verbose_name=_('Birth date'))
    native_lang = models.BooleanField(default=True, verbose_name=_('Native language ?'))
    third_time  = models.BooleanField(default=False, verbose_name=_('Has a third time ?'))
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
        m = Mark.objects.filter(student=self.id)
        return m
    
    def marks_for_course(self, course):
        marks = []
        for m in Mark.objects.filter(student=self.id):
            if m.subject.exam.course == course:
                marks.append(m)
        return marks
    
    def average(self):
        index = 0
        marks = 0
        for m in Mark.objects.filter(student=self.id):
            index = index + 1
            marks = marks + m.mark
        return marks / index
        
    def average_for_course(self, course):
        index = 0
        marks = 0
        for m in Mark.objects.filter(student=self.id):
            if m.subject.exam.course == course:
                marks = marks + m.mark
                index = index + 1
        try:
            return marks / index
        except ZeroDivisionError:
            return 0
    
    def stddev(self):
        marks = []
        for m in Mark.object.filter(student=self.id):
            mark.append(m.mark)
        try:
            return statistics.stdev(marks)
        except: #less than 2 marks : can't compute variance, exception thrown
            return 0
    
    def stddev_for_course(self, course):
        marks = []
        for m in Mark.objects.filter(student=self.id):
            if m.subject.exam.course == course:
                marks.append(m.mark)
        try:
            return statistics.stdev(marks)
        except: #less than 2 marks : can't compute variance, exception thrown
            return 0
    
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
    comment     = models.TextField(blank=True, verbose_name=_('Comments'))
    # Auto
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Mark')
    
    def __str__(self):
        return str(self.mark) + " - " + str(self.student)
        