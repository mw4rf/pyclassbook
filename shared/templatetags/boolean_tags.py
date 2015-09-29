from django import template
from django.core.urlresolvers import reverse
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name="bool_as_icon")
def bool_as_icon(boolean):
    if boolean:
        return mark_safe('<span class="glyphicon glyphicon-ok-sign text-success"></span>')
    else:
        return mark_safe('<span class="glyphicon glyphicon-remove-circle text-danger"></span>')
