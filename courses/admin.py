from django.contrib import admin

from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'level', 'start_date', 'end_date')

admin.site.register(Course, CourseAdmin)
