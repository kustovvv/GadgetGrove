from django.shortcuts import render
from django.db.models import Q

from .models import Item, Brand, Category

def details(request, pk):
    item = Item.objects.get(id=pk)
    path = f'Category {item.category.name}/Brand {item.brand.name}/Model {item.model}'
    related_items = Item.objects.filter(category=item.category).exclude(id=pk)[0:6]
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
        items = Item.objects.filter(category=category_id, availability=True)
        category = Category.objects.get(id=category_id)

        path += f'Category {category.name}/'

    if request.method == 'GET':
        action = request.GET.get('action')
        if action == 'form':
            selected_brands = request.GET.getlist('selected_brands')
            items = items.filter(brand__in=selected_brands)
            path_brands = (Brand.objects.get(id=brand) for brand in selected_brands)
            path += ', '.join(brand.name for brand in path_brands)
    
    brands = set(item.brand for item in items)
    

    request.session['navbar_state'] = 'hidden'


    return render(request, 'item/items.html', {'items': items,
                                                'brands': brands,
                                                'path': path,
                                                'category_id': int(category_id),
                                                })

def search_results(request, query):
    items = Item.objects.filter(Q(model__icontains=query) | Q(description__icontains=query) | Q(brand__name__icontains=query))

    if items:
        brands = set(item.brand for item in items)
        category_id = items[0].category.id
    
    else:
        brands = ''
        category_id = '0'   
    

    request.session['navbar_state'] = 'hidden'

    
    return render(request, 'item/items.html', {'items': items, 
                                            'brands': brands,
                                            'query': query,
                                            'category_id': int(category_id)})   
