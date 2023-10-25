from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Item, Brand, Category, Comments
from .forms import CommentForm


def details(request, pk):
    item = Item.objects.get(id=pk)
    path = f'Category {item.category.name}/Brand {item.brand.name}/Model {item.model}'
    related_items = Item.objects.filter(category=item.category).exclude(id=pk)[0:6]
    query = request.GET.get('query', '')
    comments = Comments.objects.filter(item_id=pk)

    if query:
        return search_results(request, query)

    context = {'item': item,
                'path': path,
                'related_items': related_items,
                'comments': comments
                }

    return render(request, 'item/details.html', context)

def items(request):
    query = request.GET.get('query', '')
    if query:
        return search_results(request, query)

    path = ''
    category = ''
    brands = ''

    category_id = request.GET.get('category', 0)

    if category_id:
        items = Item.objects.filter(category=category_id, availability=True)
        category = Category.objects.get(id=category_id)

    brand = request.GET.get('brand')
    if brand:
        items = items.filter(brand = brand)

    if request.method == 'GET':
        action = request.GET.get('action')
        if action == 'form':
            selected_brands = request.GET.getlist('selected_brands')
            items = items.filter(brand__in=selected_brands)
    
    items = shorten_string(items)

    brands = set(item.brand for item in items)

    path_brands = list(brands)
    if len(path_brands) > 3:
        path_brands = path_brands[:3]

    for brand in path_brands:
        path+=f'{brand.name}, '
    
    path = path[:-2] + '...'
    

    request.session['navbar_state'] = 'hidden'

    context = {'items': items,
                'brands': brands,
                'path': path,
                'category_id': int(category_id),
                'category': category,
                'path': path,
                }

    return render(request, 'item/items.html', context)

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


def shorten_string(items, max_length=33, min_length=21):
    for item in items:
        item.model = item.model[:max_length]+'...' if len(item.model) > max_length else f'{item.model}<br/>\u200E' if len(item.model) < min_length else item.model

    return items


def comments(request, pk):
    comments = Comments.objects.filter(item_id=pk)
    if comments:
        item = comments[0].item
    else:
        item = ''
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            messages.success(request, 'Your comment was saved successfully')
            comment = form.save(commit=False)
            comment.item_id = pk
            selected_rate = request.POST.getlist('inlineRadioOptions')
            if selected_rate:
                comment.rating = int(selected_rate[0])
            comment.save()

            return redirect(request.META.get('HTTP_REFERER', 'frontpage'))

        messages.error(request, 'Something wrong with your comment, please enter correct information')


    else:
        if request.user.is_authenticated:
            initial = {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,
            }
            form = CommentForm(initial=initial)
        else:
            form = CommentForm()

    return render(request, 'item/comments.html', {'form': form,
                                                  'comments': comments,
                                                  'item': item})
