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
        
    def __str__(self):
        return self.name
        

