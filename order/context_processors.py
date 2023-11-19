from .models import ShoppingCartItem

def navbar_data(request):
    if request.user.is_authenticated:
        user_cart_items = ShoppingCartItem.objects.filter(user=request.user)
        for item in user_cart_items:
            item.total_item_price = int(item.amount) * int(item.item.price)

        sellers_data = {}
        for cart_item in user_cart_items:
            seller = cart_item.item.created_by
            if seller in sellers_data:
                sellers_data[seller]['items'].append(cart_item)
                sellers_data[seller]['total_amount'] += cart_item.amount
                sellers_data[seller]['total_price'] += cart_item.total_item_price
            else:
                sellers_data[seller] = {
                    'seller': seller,
                    'items': [cart_item],
                    'total_amount': cart_item.amount,
                    'total_price': cart_item.total_item_price,
                }      

        return {'sellers_data': sellers_data}
    
    nothing = ''
    return {'nothing': nothing}