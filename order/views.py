from django.shortcuts import redirect, render
from django.contrib import messages

from .models import ShoppingCartItem,  ShippingAddress, ContactInfo, OrderItem, Order, Favorite
from item.models import Item
from .forms import ShippingAddressForm, ContactInfoForm


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
    
        return redirect(request.META.get('HTTP_REFERER', 'frontpage'))

    return redirect('login')


def delete_from_cart(request, pk):
    if request.user.is_authenticated:
        delete_it = ShoppingCartItem.objects.get(id=pk)

        delete_it.delete()
    
        return redirect(request.META.get('HTTP_REFERER', 'frontpage'))
    
    return redirect('login')


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
    
    return redirect('login')


def order(request):
    if request.user.is_authenticated:
        post_check = False

        if request.method == 'POST':
            shipping_form = ShippingAddressForm(request.POST)
            contact_form = ContactInfoForm(request.POST)

            if shipping_form.is_valid() and contact_form.is_valid():
                new_shipping_address = ShippingAddress(
                    user = request.user,
                    street_address = shipping_form.cleaned_data['street_address'],
                    city = shipping_form.cleaned_data['city'],
                    state = shipping_form.cleaned_data['state'],
                    postal_code = shipping_form.cleaned_data['postal_code'],
                    country = shipping_form.cleaned_data['country'],
                )

                new_contact_info = ContactInfo(
                    user = request.user,
                    phone_number = contact_form.cleaned_data['phone_number'],
                    first_name = contact_form.cleaned_data['first_name'],
                    last_name = contact_form.cleaned_data['last_name'],
                    email = contact_form.cleaned_data['email'],
                )

                new_contact_info.save()
                new_shipping_address.save()

                new_all_orders = Order(
                    user = request.user,
                    contact_info = new_contact_info,
                    shipping_address = new_shipping_address,
                    status = 'In processing',
                    total_price = request.POST.get('total_price', 0),
                )

                new_all_orders.save()

                items = ShoppingCartItem.objects.filter(user_id = request.user)
                
                for item in items:
                    new_customer_order = OrderItem(
                        order = new_all_orders,
                        item = item.item,
                        amount = item.amount,
                        item_price = item.item.price,
                    )

                    new_customer_order.save()

                post_check = True

                cart = ShoppingCartItem.objects.filter(user=request.user)

                cart.delete()

                return render(request, 'order/order.html', {'post_check': post_check})

        else:
            shipping_form = ShippingAddressForm()
            contact_form = ContactInfoForm()
        
        context = {'shipping_form': shipping_form,
                    'contact_form': contact_form,
                    'post_check': post_check}

        return render(request, 'order/order.html', context)

    return redirect('login')


def add_delete_favorites(request, pk):
    if request.user.is_authenticated:
        item = Item.objects.get(id=pk)
        try:
            favorites = Favorite.objects.get(user=request.user)
            
            if favorites.items.filter(id=pk).exists():
                favorites.items.remove(item)
                
            else:
                favorites.items.add(item)
                favorites.save()
            
        except:
            new_favorite = Favorite(user=request.user)
            new_favorite.save()
            new_favorite.items.add(item)
            new_favorite.save()

        return redirect(request.META.get('HTTP_REFERER', 'frontpage'))
    
    else:
        messages.error(request, 'To add an item to favorites ,you should be logged in to.')
        return redirect('login')
    
