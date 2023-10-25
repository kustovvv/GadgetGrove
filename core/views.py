from django.shortcuts import render

from item.models import Item, Category
from item.views import search_results, shorten_string


def frontpage(request):
    items = Item.objects.filter(availability=True)
    items = shorten_string(items)
    query = request.GET.get('query', '')
    categories = Category.objects.all()

    if query:
        return search_results(request, query)
            
    return render(request, 'core/frontpage.html', {'items': items,
                                            'categories': categories,
                                            })


def checking(request):
    user_personal_info = request.POST.get('user_personal_info')
    return render(request, 'core/checking.html', {'user_personal_info': user_personal_info})


