from django.shortcuts import render

from item.models import Item, Category
from item.views import search_results


def frontpage(request):
    items = Item.objects.filter(availability=True)
    query = request.GET.get('query', '')
    categories = Category.objects.all()

    if query:
        return search_results(request, query)
            
    context = {'items': items,
                'categories': categories,
                }

    return render(request, 'core/frontpage.html', context)
