from django import template

register = template.Library()

@register.filter
def list_keys(d):
    return list(d.keys())
    
@register.filter
def list_values(d):
    return list(d.values())