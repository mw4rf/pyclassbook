from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

from courses.models import Course

class Student(models.Model):
    # Fields
    firstname   = models.CharField(max_length = 100)
    lastname    = models.CharField(max_length = 100)
    email       = models.EmailField(max_length = 254)
    email_alt   = models.EmailField(max_length = 254, blank=True)
    birth       = models.DateField(null=True)
    native_lang = models.BooleanField(default=True)
    third_time  = models.BooleanField(default=False)
    # Auto
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    # Relations
    courses     = models.ManyToManyField(Course)
    
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
        return marks / index
    
    # Fields label in admin area (only for methods)
    fullname.short_description = "Name"
    
    # Fields sort order in admin area (only for methods)
    fullname.admin_order_field = 'lastname' # order by lastname
    

class Mark(models.Model):
    student     = models.ForeignKey(Student)
    subject     = models.ForeignKey('exams.Subject')
    mark        = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)])
    comment     = models.TextField(blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.mark) + " - " + str(self.student)
        