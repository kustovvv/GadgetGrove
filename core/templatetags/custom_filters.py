from django import template
from order.models import Favorite

register = template.Library()


@register.filter
def format_string(value, max_length=33, min_length=20):
    if len(value) > max_length:
        return value[:max_length]+'...' 
     
    elif len(value) < min_length:
        return f'{value}<br/>\u200E'  
    
    else:
        return value


@register.inclusion_tag('core/all_items.html')
def render_items(items, request):
    return {'items': items, 
            'request': request}


@register.inclusion_tag('core/all_items_2.html')
def render_items_2(items, order_id=''):
    return {'items': items,
            'order_id': order_id,
            }


@register.inclusion_tag('core/all_comments.html')
def render_comments(comments, your_comments=''):
    return {'comments': comments,
            'your_comments': your_comments,
            }


@register.filter
def is_in_favorites(item, user):
    return Favorite.objects.filter(user=user, items=item).exists()