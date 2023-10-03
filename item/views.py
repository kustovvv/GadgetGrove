from django.shortcuts import render

from .models import Item

def details(request, pk):
    item = Item.objects.get(id=pk)
    path = f'Category {item.category_id.name}/Brand {item.brand_id.name}/Model {item.model}'
    related_items = Item.objects.filter(category_id=item.category_id).exclude(id=pk)[0:6]
    return render(request, 'item/details.html', {'item': item,
                                                 'path': path,
                                                 'related_items': related_items,})