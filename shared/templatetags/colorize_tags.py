from django import template
from django.core.urlresolvers import reverse
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter()
def colorize_list_group_item(value, threshold):
    if value < threshold:
        return "list-group-item-danger"
    elif value == threshold:
        return "list-group-item-warning"
    else:
        return "list-group-item-success"