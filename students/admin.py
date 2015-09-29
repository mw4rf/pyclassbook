from django.contrib import admin

from .models import Student, Mark
from courses.models import Course

class MarkInline(admin.TabularInline):
    model = Mark
    extra = 0

class StudentAdmin(admin.ModelAdmin):
    inlines = [MarkInline]
    list_display = ('fullname', 'email', 'updated_at', 'native_lang', 'third_time')
    search_fields = ['firstname', 'lastname', 'email']
    list_filter = ('created_at','updated_at','native_lang','third_time',)
    ordering = ('lastname',) # -lastname for DESC order
    filter_horizontal = ('courses',)

# Register models
admin.site.register(Student, StudentAdmin)
