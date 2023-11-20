from django.shortcuts import redirect, render
from django.contrib import messages

from .models import ContactInfo, PaymentMethod, OrderStatus, ShippingAddress, Order, ShoppingCartItem, OrderItem, OrderReview
from item.models import Item
from .forms import ShippingAddressForm, ContactInfoForm
from account.models import CustomUser
from core.custom_functions import get_seller_info


def order_review(request, pk):
    if request.user.is_authenticated:
        initial_page_url = request.META.get('HTTP_REFERER', 'frontpage')
        
        order = Order.objects.get(id=pk)
        seller = order.seller
        info = get_seller_info(seller)
        seller_info = info[0]
        orders = Order.objects.filter(seller=seller)
        amount_orders = orders.count()

        if request.method == 'POST':
            review = OrderReview(
                seller = seller,
                user = request.user
            )
            selected_rate = request.POST.getlist('inlineRadioOptions', '')
            comment = request.POST.get('order_comment', '')
            if selected_rate:
                review.rating = int(selected_rate[0])
                review.comment = comment
                review.save()
                messages.success(request, 'Your comment was saved successfully')
                return redirect('account:history')
            else:
                messages.error(request, 'Please rate your order')
                context = {'order': order,
                        'seller': seller,
                        'amount_orders': amount_orders,
                        'seller_info': seller_info,
                        'input_text': comment,
                        'initial_page_url': initial_page_url,
                        }
        else:
            context = {'order': order,
                    'seller': seller,
                    'amount_orders': amount_orders,
                    'seller_info': seller_info,
                    'initial_page_url': initial_page_url,
                    }
    else:
        return redirect('login')

    return render(request, 'order/order_review.html', context)


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


def order(request, seller_id, total_price, total_amount):
    if request.user.is_authenticated:
        seller = CustomUser.objects.get(id=seller_id)
        items = ShoppingCartItem.objects.filter(user_id = request.user, item__created_by=seller)
        payment_methods = PaymentMethod.objects.all()
        selected_payment_method = request.POST.get('selected_payment_method', 1)
        payment_method = PaymentMethod.objects.get(id=int(selected_payment_method))
        order_comment = request.POST.get('order_comment', '')
        status = OrderStatus.objects.get(status='In progress')

        if selected_payment_method == '1':
            payment_check = True
        else:
            payment_check = False

        if request.method == 'POST':
            shipping_form = ShippingAddressForm(request.POST)
            contact_form = ContactInfoForm(request.POST)

            if shipping_form.is_valid() and contact_form.is_valid():
                new_shipping_address = ShippingAddress.objects.get_or_create(
                    user = request.user,
                    street_address = shipping_form.cleaned_data['street_address'],
                    city = shipping_form.cleaned_data['city'],
                    state = shipping_form.cleaned_data['state'],
                    postal_code = shipping_form.cleaned_data['postal_code'],
                    country = shipping_form.cleaned_data['country'],
                )[0]

                new_contact_info = ContactInfo.objects.get_or_create(
                    user = request.user,
                    phone_number = contact_form.cleaned_data['phone_number'],
                    first_name = contact_form.cleaned_data['first_name'],
                    last_name = contact_form.cleaned_data['last_name'],
                    email = contact_form.cleaned_data['email'],
                )[0]

                new_contact_info.save()
                new_shipping_address.save()

                new_all_orders = Order(
                    user = request.user,
                    seller = seller,
                    contact_info = new_contact_info,
                    shipping_address = new_shipping_address,
                    status = status,
                    payment_method = payment_method,
                    total_price = total_price,
                    comment = order_comment,
                )

                new_all_orders.save()
                
                for item in items:
                    new_customer_order = OrderItem(
                        order = new_all_orders,
                        item = item.item,
                        amount = item.amount,
                        item_price = item.item.price,
                    )

                    new_customer_order.save()

                cart = ShoppingCartItem.objects.filter(user=request.user, item__created_by=seller)

                cart.delete()

                return render(request, 'order/success.html', {'payment_check': payment_check})

        else:
            shipping_form = ShippingAddressForm()
            contact_form = ContactInfoForm()
        
        context = {'shipping_form': shipping_form,
                    'contact_form': contact_form,
                    'payment_methods': payment_methods,
                    'payment_method': payment_method,
                    'total_amount': total_amount,
                    'total_price': total_price,
                    'items': items,
                    }

        return render(request, 'order/order.html', context)

    return redirect('login')