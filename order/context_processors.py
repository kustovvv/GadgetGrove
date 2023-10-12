from .models import ShoppingCartItem

from django.shortcuts import render

def navbar_data(request):
    if request.user.is_authenticated:
        user_cart_items = ShoppingCartItem.objects.filter(user=request.user)
        
        total_price = 0
        for item in user_cart_items:
            item.total_item_price = int(item.amount) * int(item.item.price)
        
            total_price += item.total_item_price

        return {'user_cart_items': user_cart_items,
                'total_price': total_price}
    
    nothing = ''
    return {'nothing': nothing}