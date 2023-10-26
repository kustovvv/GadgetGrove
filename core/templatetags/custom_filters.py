from django import template

register = template.Library()


@register.filter
def format_string(value, max_length=33, min_length=20):
    if len(value) > max_length:
        return value[:max_length]+'...' 
     
    elif len(value) < min_length:
        return f'{value}<br/>\u200E'  
    
    else:
        return value
