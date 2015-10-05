from django import template
from django.core.urlresolvers import reverse
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name="bool_as_icon")
def bool_as_icon(boolean):
    if boolean:
        return mark_safe('<i class="check circle icon green"></i>')
    else:
        return mark_safe('<i class="remove circle icon red"></i>')
