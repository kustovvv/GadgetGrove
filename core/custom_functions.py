from django.shortcuts import render
from django.db.models import Q

from account.models import PersonalInformation
from order.models import Order
from item.models import Item, Brand


def get_seller_info(seller):
    try:
        seller_info = PersonalInformation.objects.get(user=seller)

        seller_additional_info = {
            'Facebook': seller_info.facebook,
            'Instagram': seller_info.instagram,
            'Twitter': seller_info.twitter,
            'Google': seller_info.google,
            'Pinterest': seller_info.pinterest,
        }
        orders = Order.objects.filter(seller__id=seller)
        if orders:
            amount_orders = orders.count()

    except:
        seller_info = ''
        seller_additional_info = ''
        amount_orders = ''

    return seller_info, seller_additional_info, amount_orders


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