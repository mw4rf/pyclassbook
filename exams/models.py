from django.db import models
from datetime import date

import uuid

class Exam(models.Model):
    # UUID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Fields
    name =          models.CharField(max_length = 254, default='')
    course =        models.ForeignKey('courses.Course')
    date =          models.DateField(blank=True, null=True)
    time_allowed =  models.IntegerField(blank=True, null=True)
    place =         models.CharField(max_length = 254, default='')
    comments =      models.TextField(blank=True, default='')
    # Auto
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name + " (" + str(self.course) + ")"
        
    def subjects(self):
        return Subject.objects.filter(exam=self.id)
    
class Subject(models.Model):
    # UUID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Fields
    exam =      models.ForeignKey(Exam)
    title =     models.TextField(blank=True, default='')
    kind =      models.CharField(max_length = 254, default='')
    # Auto
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.exam) + "(" + self.kind + ")"
    
