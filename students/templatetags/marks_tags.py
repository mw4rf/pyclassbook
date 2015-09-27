from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(needs_autoescape=True)
def colorize_mark(mark, autoescape=True):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    result = ''
    if mark >= 10:
        result = '<span class="text-success">%s</span>' % (esc(mark))
    elif mark < 10:
        result = '<span class="text-danger">%s</span>' % (esc(mark))
    return mark_safe(result)