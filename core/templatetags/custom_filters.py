from django import template
from item.models import FavoriteCompare

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
            'request': request
            }


@register.inclusion_tag('core/all_items_2.html')
def render_items_2(items, order_id=''):
    return {'items': items,
            'order_id': order_id,
            }


@register.inclusion_tag('core/all_comments.html')
def render_comments(comments, your_comments=''):
    for comment in comments:
        if comment.rating:
            comment.stars = range(comment.rating)
            comment.hollow_stars = range(5-comment.rating)
    return {'comments': comments,
            'your_comments': your_comments,
            }


@register.filter
def is_in_favorites(item, user):
    return FavoriteCompare.objects.filter(user=user, favorite_items=item).exists()


@register.filter
def is_in_compare(item, user):
    return FavoriteCompare.objects.filter(user=user, compare_items=item).exists()


@register.inclusion_tag('conversation/conversation_template.html')
def render_conversation(conversation, request):
    return {'conversation': conversation,
            'request': request}


@register.inclusion_tag('item/item_stars.html')
def render_item_stars(item):
    sum = 0
    avg_rating = 4
    count = 0
    comments = item.comments.all()
    for comment in comments:
        if comment.rating:
            sum+=comment.rating
            count+=1
    if count:
        avg_rating = round(sum/count)
    item.stars = range(avg_rating)
    item.hollow_stars = range(5-avg_rating)

    return {'item': item}