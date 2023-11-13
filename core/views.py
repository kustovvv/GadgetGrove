from django.shortcuts import render

from item.models import Category, Item
from item.views import search_results


def frontpage(request):
    if request.user.is_authenticated:
        items = Item.objects.filter(availability=True).exclude(created_by=request.user)
    else:
        items = Item.objects.filter(availability=True)

    query = request.GET.get('query', '')
    categories = Category.objects.all()

    if query:
        return search_results(request, query)
            
    context = {'items': items,
                'categories': categories,
                }

    return render(request, 'core/frontpage.html', context)
