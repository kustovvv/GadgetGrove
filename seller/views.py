from django.shortcuts import render

from item.models import Item
from order.models import OrderReview
from core.custom_functions import get_seller_info, search_results

def seller_catalog(request, seller_id):
    option = 'catalog'
    query = request.GET.get('query', '')
    if query:
        return search_results(request, query)
    items = Item.objects.filter(created_by__id=seller_id)
    selected_category = request.GET.get('category', '')
    categories = set(item.category_brand.category for item in items)
    if selected_category:
        items = items.filter(category_brand__category=selected_category)
    
    info = get_seller_info(seller_id)
    seller_info = info[0]
    amount_orders = info[2]

    context = {'amount_orders': amount_orders,
               'items': items,
               'categories': categories,
               'seller_info': seller_info,
               'amount_orders': amount_orders,
               'option': option,
               }
    return render(request, 'seller/seller_catalog.html', context)


def seller_reviews(request, seller_id):
    option = 'reviews'
    query = request.GET.get('query', '')
    if query:
        return search_results(request, query)
    reviews = OrderReview.objects.filter(seller=seller_id)
    info = get_seller_info(seller_id)
    seller_info = info[0]
    amount_orders = info[2]

    context = {'reviews': reviews,
               'seller_info': seller_info,
               'amount_orders': amount_orders,
               'option': option,
                }
    
    return render(request, 'seller/seller_reviews.html', context)


def seller_contacts(request, seller_id):
    option = 'contacts'
    query = request.GET.get('query', '')
    if query:
        return search_results(request, query)
    info = get_seller_info(seller_id)
    seller_info = info[0]
    seller_additional_info = info[1]
    amount_orders = info[2]
    flag = any(value for value in seller_additional_info.values())
    if not flag:
        seller_additional_info = False


    context = {'seller_info': seller_info,
               'amount_orders': amount_orders,
               'seller_additional_info': seller_additional_info,
               'option': option,
                }
    
    return render(request, 'seller/seller_contacts.html', context)


def seller_schedule(request, seller_id):
    option = 'schedule'
    query = request.GET.get('query', '')
    if query:
        return search_results(request, query)
    info = get_seller_info(seller_id)
    seller_info = info[0]
    amount_orders = info[2]

    context = {'seller_info': seller_info,
               'amount_orders': amount_orders,
               'option': option,
                }
    
    return render(request, 'seller/seller_schedule.html', context)


def seller_about(request, seller_id):
    option = 'about'
    query = request.GET.get('query', '')
    if query:
        return search_results(request, query)
    info = get_seller_info(seller_id)
    seller_info = info[0]
    amount_orders = info[2]

    context = {'seller_info': seller_info,
               'amount_orders': amount_orders,
               'option': option,
                }
    
    return render(request, 'seller/seller_about.html', context)