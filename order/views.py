from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import ShoppingCartItem, OrderItem, Order
from item.models import Item


@login_required
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


@login_required
def delete_from_cart(request, pk):
    if request.user.is_authenticated:
        delete_it = ShoppingCartItem.objects.get(id=pk)

        delete_it.delete()
    
    request.session['navbar_state'] = 'visible'

    return redirect(request.META.get('HTTP_REFERER', 'frontpage'))


@login_required
def change_amount_items(request, pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            action = request.POST.get('action')
            if action:
                cart_item = ShoppingCartItem.objects.get(id=pk, user_id=request.user)
                if action == 'increase':
                    cart_item.amount += 1
                
                elif action == 'decrease':
                    if cart_item.amount > 1:
                        cart_item.amount -= 1
                
                cart_item.save()
    
    return redirect(request.META.get('HTTP_REFERER', 'frontpage'))


@login_required
def order(request):
    return render(request, 'order/order.html')


@login_required
def add_to_order_items(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            total_price = request.POST.get('total_price', 0)

            new_all_orders = Order(
                user = request.user,
                status = 'In processing',
                total_price = total_price,
            )

            new_all_orders.save()

            items = ShoppingCartItem.objects.filter(user_id = request.user)
            
            for item in items:
                new_customer_order = OrderItem(
                    order = new_all_orders.id,
                    item = item.item.id,
                    amount = item.amount,
                    item_price = item.item.price,
                )

                new_customer_order.save()