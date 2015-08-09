from django.contrib import admin

from .models import Exam, Subject

class SubjectInline(admin.StackedInline):
    model = Subject
    extra = 0

class ExamAdmin(admin.ModelAdmin):
    inlines = [SubjectInline]
    list_display = ('name', 'date', 'course', 'place', 'time_allowed')

# Register models
admin.site.register(Exam, ExamAdmin)
admin.site.register(Subject)
