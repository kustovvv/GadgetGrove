from django.shortcuts import render

from item.models import Item
from order.models import Order, OrderReview
from account.models import PersonalInformation

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
        amount_orders = orders.count()

    except:
        seller_info = ''
        seller_additional_info = ''
        amount_orders = ''

    return seller_info, seller_additional_info, amount_orders


def seller_catalog(request, seller_id):
    option = 'catalog'
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
    info = get_seller_info(seller_id)
    seller_info = info[0]
    amount_orders = info[2]

    context = {'seller_info': seller_info,
               'amount_orders': amount_orders,
               'option': option,
                }
    
    return render(request, 'seller/seller_about.html', context)