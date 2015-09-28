from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()
    
@register.filter(name="course_years")
def course_years(course):
    return '%s-%s' % (course.start_date.year, course.end_date.year)
