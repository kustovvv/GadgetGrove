from django.shortcuts import render

from .models import Item

def phone(request):
    items = Item.objects.all()
    if phone:
        return render(request, 'core/frontpage.html')
    else:
        return render(request, 'item/items.html', {'phones': items})