from django.db import models

import uuid

class Course(models.Model):
    # UUID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Fields
    name =          models.CharField(max_length = 254)
    level =         models.CharField(max_length=10, blank=True)
    place =         models.CharField(max_length = 254, blank=True)
    kind =          models.CharField(max_length = 254, blank=True)
    comments =      models.TextField(blank=True)
    start_date =    models.DateField(blank=True)
    end_date =      models.DateField(blank=True)
    # Auto
    created_at =    models.DateTimeField(auto_now_add=True)
    updated_at =    models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.name
        

