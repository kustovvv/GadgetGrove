from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages

from .models import CategoryBrand, Category, Brand, FavoriteCompare, Comments, Item
from account.models import PersonalInformation
from .forms import CommentForm

def add_update_item(request):
    if request.user.is_authenticated:
        item_id = request.GET.get('item_id', '')
        if request.method == 'POST':
            item_id = request.POST.get('item_id', '')
            
            item = get_object_or_404(Item, id=int(item_id)) if item_id else Item()
            fields = {
                'model': request.POST.get('new_title_input'),
                'price': request.POST.get('new_price_input')
            }
            for field, value in fields.items():
                if not value:
                    messages.error(request, f'The {field} field must be filled in!')
                    return redirect(request.META.get('HTTP_REFERER', 'frontpage'))
            
            selected_category = request.POST.get('category-select-item')
            selected_brand = request.POST.get('brand-select')
            if selected_category=='-1' or selected_brand=='-1':
                messages.error(request, 'Category and brand should be selected.')
                return redirect(request.META.get('HTTP_REFERER', 'frontpage'))
            
            category_brand = CategoryBrand.objects.get(category=int(selected_category), brand=int(selected_brand))

            availability = request.POST.get('is_available', False)
            if availability:
                availability = True

            image = request.FILES.get('new_image')
            
            if not image:
                if item_id:
                    image = item.image

            item.created_by = request.user
            item.category_brand = category_brand
            item.model = fields['model']
            item.description = request.POST.get('new_description_input')
            item.price = fields['price']
            item.image = image
            item.availability = availability

            item.save()

            if item_id:
                messages.success(request, 'Your ad was updated successfully')
                return redirect(request.META.get('HTTP_REFERER', 'frontpage'))

            messages.success(request, 'Your ad was added successfully')
            return redirect('frontpage')
        else:
            selected_brand = ''
            item = ''
            all_categories = Category.objects.all()
            selected_category = request.GET.get('category', '-1')

            brands = Brand.objects.all()

            if item_id:
                item = Item.objects.get(id=item_id)
                if selected_category == '-1':
                    selected_category = str(item.category_brand.category.id)
                selected_brand = item.category_brand.brand.id

            if selected_category:
                if selected_category != '-1':
                    brands = Brand.objects.filter(category_brands__category_id=int(selected_category))                
                    
            context = {'all_categories': all_categories,
                       'brands': brands,
                       'selected_category': int(selected_category),
                       'selected_brand': selected_brand,
                       'item': item,
                       'item_id': item_id
                       }

            return render(request, 'item/add_update_item.html', context)
    
    return redirect('login')


def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()

    messages.success(request, 'The item was removed successfully')
    return redirect('account:ads')


def delete_items(request):
    selected_items = request.GET.get('selectedValues')
    selected_items = selected_items.split(',')
    if selected_items:
        for value in selected_items:
            if value:
                item = get_object_or_404(Item, pk=int(value))
                item.delete()
            else:
                messages.success(request, 'No item selected')
                return redirect('account:ads')
        messages.success(request, 'The items was removed successfully')
        return redirect('account:ads')
    
    
def details(request, pk):
    item = Item.objects.get(id=pk)
    related_items = Item.objects.filter(category_brand=item.category_brand).exclude(id=pk)[0:6]
    query = request.GET.get('query', '')
    comments = Comments.objects.filter(item_id=pk)
    seller_info = PersonalInformation.objects.get(user=item.created_by)

    seller_additional_info = {
        'Facebook': seller_info.facebook,
        'Instagram': seller_info.instagram,
        'Twitter': seller_info.twitter,
        'Google': seller_info.google,
        'Pinterest': seller_info.pinterest,
    }
    
    if query:
        return search_results(request, query)

    context = {'item': item,
                'related_items': related_items,
                'comments': comments,
                'seller_info': seller_info,
                'seller_additional_info': seller_additional_info,
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
        items = Item.objects.filter(category_brand__category=category_id, availability=True).exclude(created_by=request.user)
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
    items = Item.objects.filter(Q(model__icontains=query) | Q(description__icontains=query) | Q(category_brand__brand__name__icontains=query)).exclude(created_by=request.user)

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
    query = request.GET.get('query', '')
    if query:
        return search_results(request, query)
    
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


def favorites(request):
    if request.user.is_authenticated:
        option = 'favorites'
        query = request.GET.get('query', '')
        if query:
            return search_results(request, query)
        
        user_items = FavoriteCompare.objects.get_or_create(user=request.user)[0]
        items = user_items.favorite_items.all()
        all_categories = set(item.category_brand.category for item in items)
        selected_category = request.GET.get('category', '-1')
        input = request.GET.get('input', '')

        if input:
            items = items.filter(model__icontains=input)
        
        if selected_category:
            if selected_category != '-1':
                items = items.filter(category_brand__category = selected_category)

        context = {'option': option,
                   'items': items,
                   'all_categories': all_categories,
                   'selected_category': int(selected_category),
                   }

        return render(request, 'account/account_favorites.html', context)
    
    return redirect('login')


def add_delete_favorites_compare(request, pk):
    if request.user.is_authenticated:
        item = Item.objects.get(id=pk)
        model_instance = FavoriteCompare.objects.get_or_create(user=request.user)[0]
        model_option = request.GET.get('model_option', '')
        if model_option:
            items = model_instance.favorite_items
        else:
            items = model_instance.compare_items

        if items.filter(id=pk).exists():
            items.remove(item)
        else:  
            items.add(item)
            model_instance.save()

        return redirect(request.META.get('HTTP_REFERER', 'frontpage'))
    
    else:
        messages.error(request, 'To add an item to favorites or compares, you should be logged in to')
        return redirect('login')
    

def compare(request):
    if request.user.is_authenticated:
        query = request.GET.get('query', '')
        if query:
            return search_results(request, query)
        
        all_items = FavoriteCompare.objects.get_or_create(user=request.user)[0]
        user_items = all_items.compare_items.all()
        categories = ''
        selected_category = '0'
        items = ''

        if user_items:
            categories = list(set(item.category_brand.category for item in user_items))
            selected_category = request.GET.get('selected_category', categories[0].id)
            items = user_items.filter(category_brand__category=selected_category)

        context = {'items': items,
                   'categories': categories,
                   'selected_category': int(selected_category),
                   }
        
        return render(request, 'item/compare.html', context)
    else:
        return redirect('login')