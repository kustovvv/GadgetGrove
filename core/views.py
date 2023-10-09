from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import SignUpForm

from item.models import Item, Category
from item.views import search_results


def frontpage(request):
    items = Item.objects.filter(availability=True)
    query = request.GET.get('query', '')
    categories = Category.objects.all()

    if query:
        return search_results(request, query)
        
    return render(request, 'core/frontpage.html', {'items': items,
                                                   'categories': categories,
                                                   })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('item:items')
    else:
        form = SignUpForm()

    request.session['navbar_state'] = 'hidden'

    return render(request, 'core/signup.html', {'form': form})
