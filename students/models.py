from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    firstname   = models.CharField(max_length = 100)
    lastname    = models.CharField(max_length = 100)
    email       = models.EmailField(max_length = 254)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.fullname()
        
    def fullname(self):
        return self.firstname + " " + self.lastname
    
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
        