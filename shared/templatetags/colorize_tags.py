from django import template
from django.core.urlresolvers import reverse
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def colorize_label_average(avg):
    if avg > 10:
        return "green"
    elif avg == 10:
        return "orange"
    else:
        return "red"
        
@register.filter
def colorize_label_stddev(stddev):
    if stddev > 2:
        return "red"
    if stddev > 1:
        return "orange"
    else:
        return "green"
        
@register.filter
def colorize_label_mark(mark):
    return colorize_label_average(mark)