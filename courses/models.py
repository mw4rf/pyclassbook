from django.db import models

class Course(models.Model):
    name =          models.CharField(max_length = 254)
    level =         models.CharField(max_length=10, blank=True)
    place =         models.CharField(max_length = 254, blank=True)
    comments =      models.TextField(blank=True)
    start_date =    models.DateField(blank=True)
    end_date =      models.DateField(blank=True)
    created_at =    models.DateTimeField(auto_now_add=True)
    updated_at =    models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
