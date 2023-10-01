from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import SignUpForm

from item.models import Item, Brand, Category

def frontpage(request):
    items = Item.objects.filter(availability=True)[0:10]
    categories = Category.objects.all()
    brands = Brand.objects.all()

    return render(request, 'core/frontpage.html', {'items': items,
                                                   'categories': categories,
                                                   'brands': brands})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('item:items')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})
    