from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='average_for_course')
def average_for_course(student, course):
    return student.average_for_course(course)
    
@register.filter(name='marks_for_course')
def marks_for_course(student, course):
    return student.marks_for_course(course)
    
@register.filter(needs_autoescape=True, name="courses_for_student")
def courses_for_student(courses, autoescape=True):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    result = ""
    for c in courses:
        result = result + '<span class="label label-default"><a href="/courses/%s/">%s</a></span> ' % (esc(c.id), esc(c.name))
    return mark_safe(result)
