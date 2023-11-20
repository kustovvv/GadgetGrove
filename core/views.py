from django.shortcuts import render

from item.models import Category, Item
from core.custom_functions import search_results


def frontpage(request):
    if request.user.is_authenticated:
        items = Item.objects.all().exclude(created_by=request.user)
    else:
        items = Item.objects.all()

    query = request.GET.get('query', '')
    categories = Category.objects.all()

    if query:
        return search_results(request, query)
            
    context = {'items': items,
                'categories': categories,
                }

    return render(request, 'core/frontpage.html', context)
