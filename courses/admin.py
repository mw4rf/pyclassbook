from django.contrib import admin

from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'level', 'kind', 'start_date', 'end_date')
    search_fields = ['name', 'place', 'level', 'kind']
    list_filter = ('place','level','kind','start_date', 'end_date')
    ordering = ('start_date',) # -start_date for DESC order

admin.site.register(Course, CourseAdmin)
