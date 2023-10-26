from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages

from .models import Item, Comments, CategoryBrand, Category, Brand
from .forms import CommentForm


def details(request, pk):
    item = Item.objects.get(id=pk)
    related_items = Item.objects.filter(category_brand=item.category_brand).exclude(id=pk)[0:6]
    query = request.GET.get('query', '')
    comments = Comments.objects.filter(item_id=pk)

    if query:
        return search_results(request, query)

    context = {'item': item,
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
        items = Item.objects.filter(category_brand__category=category_id, availability=True)
        category = Category.objects.get(id=category_id)

    brand_id = request.GET.get('brand')
    if brand_id:
        items = items.filter(category_brand__brand = brand_id)

    if request.method == 'GET':
        action = request.GET.get('action')
        if action == 'form':
            selected_brands = request.GET.getlist('selected_brands')
            items = items.filter(category_brand__brand__in=selected_brands)

    brands = Brand.objects.filter(category_brands__category=category_id)

    path_brands = list(brands)

    if len(path_brands) > 3:
        path_brands = path_brands[:3]

    for brand in path_brands:
        path += f'{brand.name}, '
    
    path = path[:-2] + '...'
    
    context = {'items': items,
                'brands': brands,
                'path': path,
                'category_id': int(category_id),
                'category': category,
                'path': path,
                }

    return render(request, 'item/items.html', context)


def search_results(request, query):
    items = Item.objects.filter(Q(model__icontains=query) | Q(description__icontains=query) | Q(category_brand__brand__name__icontains=query))

    if items:
        category_id = items[0].category_brand.category.id
        brands = Brand.objects.filter(category_brands__category=category_id)
    
    else:
        brands = ''
        category_id = '0'   
    
    context = {'items': items, 
                'brands': brands,
                'query': query,
                'category_id': int(category_id)}
    
    return render(request, 'item/items.html', context)   


def comments(request, pk):
    comments = Comments.objects.filter(item_id=pk)
    item = Item.objects.get(id=pk)
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

    context = {'form': form,
                'comments': comments,
                'item': item,
                }

    return render(request, 'item/comments.html', context)
