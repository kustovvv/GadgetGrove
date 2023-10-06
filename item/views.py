from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Item, Brand, Category

def details(request, pk):
    item = Item.objects.get(id=pk)
    path = f'Category {item.category_id.name}/Brand {item.brand_id.name}/Model {item.model}'
    related_items = Item.objects.filter(category_id=item.category_id).exclude(id=pk)[0:6]
    query = request.GET.get('query', '')

    if query:
        return search_results(request, query)

    return render(request, 'item/details.html', {'item': item,
                                                 'path': path,
                                                 'related_items': related_items,})

def items(request):
    query = request.GET.get('query', '')
    if query:
        return search_results(request, query)

    path = ''
    category_id = request.GET.get('category', 0)

    if category_id:
        items = Item.objects.filter(category_id=category_id, availability=True)
        category = Category.objects.get(id=category_id)

        path += f'Category {category.name}/'

    brands = set(item.brand_id for item in items)

    if request.method == 'GET':
        action = request.GET.get('action')
        if action == 'form':
            selected_brands = request.GET.getlist('selected_brands')
            items = items.filter(brand_id__in=selected_brands)
            path_brands = (Brand.objects.get(id=brand) for brand in selected_brands)
            path += ', '.join(brand.name for brand in path_brands)


    return render(request, 'item/items.html', {'items': items,
                                                'brands': brands,
                                                'path': path,
                                                'category_id': int(category_id)
                                                })

def search_results(request, query):
    items = Item.objects.filter(Q(model__icontains=query) | Q(description__icontains=query))
    brands = set(item.brand_id for item in items)
    category_id = items[0].category_id.id
    return render(request, 'item/items.html', {'items': items, 
                                            'brands': brands,
                                            'query': query,
                                            'category_id': int(category_id)})   
