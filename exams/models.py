from django.db import models
from datetime import date
from django.utils.translation import ugettext as _

import uuid

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
        
    def subjects(self):
        return Subject.objects.filter(exam=self.id)
    
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
    
