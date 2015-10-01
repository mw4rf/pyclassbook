from django import template

register = template.Library()

@register.simple_tag
def sort_row(request, field, value):
    '''http://stackoverflow.com/questions/2272370/sortable-table-columns-in-django
    In Template : <th><a href="?{% sort_row request 'order_by' 'name' %}">Name</a></th>
    '''
    dict_ = request.GET.copy()
    if field == 'order_by' and field in dict_.keys():          
        if dict_[field].startswith('-') and dict_[field].lstrip('-') == value:
            # click twice on same column, revert ascending/descending            
            dict_[field] = value
        else:
            dict_[field] = "-"+value
    else:
        dict_[field] = value
    return dict_.urlencode()