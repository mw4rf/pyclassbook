from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def average_for_course(student, course):
    return student.average_for_course(course)

@register.filter
def stddev_for_course(student, course):
    return student.stddev_for_course(course)
    
@register.filter
def marks_for_course(student, course):
    return student.marks_for_course(course)

@register.filter
def count_marks_for_course(student, course):
    return len(student.marks_for_course(course))

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

@register.filter(needs_autoescape=True)
def future_average(student, course, autoescape=True):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
        
    current = student.average_for_course(course)
    dic = student.future_average(course)
    result = "<thead><tr>"
    
    # Marks
    for mark in dic.keys():
        if dic[mark] < current:
            css = 'class="danger"'
        elif dic[mark] == current:
            css = 'class="warning"'
        else:
            css = 'class="success"'
        result = result + '<th %s>%s</th>' % (css, esc(mark))
        
    result = result + "</tr></thead>\n<tbody><tr>"
    
    # New average
    for average in dic.values():
        if average < current:
            css = 'class="danger"'
        elif average == current:
            css = 'class="warning"'
        else:
            css = 'class="success"'
        result = result + '<td %s>%s</td>' % (css, esc(average))
    
    result = result + "</tr>\n<tr>"
    
    # Delta (difference between old and new average)
    for average in dic.values():
        delta = float("{0:.1f}".format(average - current))
        if delta < 0:
            css = 'class="danger"'
        elif delta == 0:
            css = 'class="warning"'
            delta = "="
        else:
            css = 'class="success"'
            delta = "+" + str(delta)
        result = result + '<td %s>%s</td>' % (css, esc(delta))
    
    result = result + "</tr></tbody>"
    return mark_safe(result)