from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.db.models import Q

from .forms import SignUpForm

from item.models import Item, Brand, Category

def frontpage(request):
    items = Item.objects.filter(availability=True)
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    brand_id = request.GET.get('brand', 0)
    brands = Brand.objects.all()

    path = ''
    if category_id:
        items = Item.objects.filter(category_id=category_id)
        brands = set(item.brand_id for item in items)
        category = Category.objects.get(id=category_id)

        path += f'Category {category.name}/'

    if brand_id:
        items = items.filter(brand_id=brand_id)
        brand = Brand.objects.get(id=brand_id)
        path += f'Brand {brand.name}/'

    if query:
        items = items.filter(Q(model__icontains=query) | Q(description__icontains=query))

    categories = Category.objects.all()

    return render(request, 'core/frontpage.html', {'items': items,
                                                   'categories': categories,
                                                   'brands': brands,
                                                   'category_id':int(category_id),
                                                   'path': path,
                                                   })

def signup(request):
    is_login_or_signup_page = request.path 
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('item:items')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})
    