from django.db import models
from datetime import date

class Exam(models.Model):
    name =          models.CharField(max_length = 254, default='')
    course =        models.ForeignKey('courses.Course')
    date =          models.DateField(blank=True, null=True)
    time_allowed =  models.IntegerField(blank=True, null=True)
    place =         models.CharField(max_length = 254, default='')
    comments =      models.TextField(blank=True, default='')
    
    def __str__(self):
        return self.name + " (" + str(self.course) + ")"
        
    def subjects(self):
        return Subject.objects.filter(exam=self.id)
    
class Subject(models.Model):
    exam =      models.ForeignKey(Exam)
    title =     models.TextField(blank=True, default='')
    kind =      models.CharField(max_length = 254, default='')
    
    def __str__(self):
        return str(self.exam) + "(" + self.kind + ")"
    
