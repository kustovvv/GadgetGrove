from django.shortcuts import redirect

from .models import ShoppingCartItem
from item.models import Item

def add_to_cart(request, pk, amount):
    if request.user.is_authenticated:
        try:
            cart_item = ShoppingCartItem.objects.get(item_id=pk, user_id=request.user)
            cart_item.amount += 1
        except ShoppingCartItem.DoesNotExist:
            cart_item = ShoppingCartItem(
                user = request.user,
                item = Item.objects.get(id=pk),
                amount = amount,
            )

        cart_item.save()
    
    request.session['navbar_state'] = 'hidden'

    return redirect(request.META.get('HTTP_REFERER', 'frontpage'))


def delete_from_cart(request, pk):
    if request.user.is_authenticated:
        delete_it = ShoppingCartItem.objects.get(id=pk)

        delete_it.delete()
    
    request.session['navbar_state'] = 'visible'

    return redirect(request.META.get('HTTP_REFERER', 'frontpage'))


# def toggle_navbar(request):
#     if request.method == 'GET':
#         navbar_state = request.GET.get('navbar_state', 'hidden')

#         request.session['navbar_state'] = navbar_state
    
#     return redirect(request.META.get('HTTP_REFERER', 'frontpage'))

    