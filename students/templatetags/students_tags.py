from django import template

register = template.Library()

@register.filter(name='average_for_course')
def average_for_course(student, course):
    return student.average_for_course(course)
    
@register.filter(name='marks_for_course')
def marks_for_course(student, course):
    return student.marks_for_course(course)
    
@register.filter
def format_courses(courses):
    result = ""
    for c in courses:
        result = result + c.name + " "
    return result