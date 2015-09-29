from django.contrib import admin

from .models import Exam, Subject

class SubjectInline(admin.StackedInline):
    model = Subject
    extra = 0

class ExamAdmin(admin.ModelAdmin):
    inlines = [SubjectInline]
    list_display = ('name', 'date', 'course', 'place', 'time_allowed')
    search_fields = ['name', 'course', 'place', 'time_allowed', 'date']
    list_filter = ('name', 'course', 'place', 'time_allowed', 'date',)
    ordering = ('date',) # -date for DESC order

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('exam', 'kind', 'created_at')
    search_fields = ['exam', 'kind']
    list_filter = ('kind', 'created_at', 'updated_at',)
    ordering = ('created_at',) # -date for DESC order

# Register models
admin.site.register(Exam, ExamAdmin)
admin.site.register(Subject, SubjectAdmin)
