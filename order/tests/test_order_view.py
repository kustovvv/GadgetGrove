import pytest
from django.urls import reverse

from authentication.models import User
from account.models import PersonalInformation
from order.models import Order, OrderReview, ShoppingCartItem

@pytest.mark.test_order_view
def test_order_view_order_review(db, client_user, custom_user_factory, personal_information_factory, order_factory):
    client, user = client_user
    seller = custom_user_factory.create()
    personal_information_factory.create(user=seller)
    order = order_factory.create(user=user, seller=seller)
    
    url = reverse('order:order_review', args=[order.id])
    response = client.post(url)

    assert response.status_code == 200
    assert PersonalInformation.objects.count() == 1
    assert response.context['order'] == order
    assert response.context['seller'] == seller
    assert response.context['amount_orders'] == 1


@pytest.mark.test_order_view
def test_order_view_order_review_POST(db, client_user, custom_user_factory, order_status_factory, payment_method_factory, order_factory):
    client, user = client_user
    seller = custom_user_factory.create()
    order_status = order_status_factory.create()
    payment_method = payment_method_factory.create()
    for _ in range(2):
        order_factory.create(seller=seller, status=order_status, payment_method=payment_method)
    order_factory.create(status=order_status, payment_method=payment_method)
    order = order_factory.create(user=user, seller=seller, status=order_status, payment_method=payment_method)
    
    rating = '5'
    order_comment = 'Test order comment'

    data = {
        'inlineRadioOptions': list(rating),
        'order_comment': order_comment,
    }

    url = reverse('order:order_review', args=[order.id])
    response = client.post(url, data=data)

    order_review = OrderReview.objects.last()

    assert response.status_code == 302
    assert Order.objects.count() == 4
    assert OrderReview.objects.count() == 1
    assert order_review.order == order
    assert order_review.rating == int(rating)
    assert order_review.comment == order_comment


@pytest.mark.test_order_view
def test_order_view_add_to_cart(db, client_user, item_factory):
    client, user = client_user
    item = item_factory.create()
    amount = 1
    url = reverse('order:add_to_cart', args=[item.id, amount])
    response = client.get(url)
    
    shopping_cart_item = ShoppingCartItem.objects.last()

    assert response.status_code == 302
    assert ShoppingCartItem.objects.count() == 1
    assert shopping_cart_item.item == item
    assert shopping_cart_item.user == user
    assert shopping_cart_item.amount == amount


# @pytest.mark.test_order_view
# def test_order_view_delete_from_cart(db, client_user, item_factory, shopping_cart_item_factory):
#     client, user = client_user
#     item = item_factory.create()
#     amount = 3
#     shopping_cart_item = ShoppingCartItem.objects.create(user=user, item=item, amount=amount)
#     shopping_cart_item.save()
    
#     shopping_cart_item = ShoppingCartItem.objects.get(user=user)
#     assert shopping_cart_item.item == item
#     assert shopping_cart_item.amount == amount

#     url = reverse('order:delete_from_cart', args=[item.id])
#     response = client.get(url)

#     assert response.status_code == 302
#     assert ShoppingCartItem.objects.count() == 0


# @pytest.mark.test_order_view
# def test_order_view_change_amount_items(db, client_user, item_factory, shopping_cart_item_factory):
#     client, user = client_user
#     item = item_factory.create()
#     amount = 3
#     shopping_cart_item_factory.create(user=user, item=item, amount=amount)

#     data = {
#         'action': 'increase',
#     }
#     shopping_cart_item = ShoppingCartItem.objects.last()

#     assert shopping_cart_item.amount == amount

#     url = reverse('order:change_amount_items', args=[item.id])
#     response = client.post(url, data=data)
#     shopping_cart_item = ShoppingCartItem.objects.last()

#     assert response.status_code == 302
#     assert shopping_cart_item.amount == amount+1

#     data = {
#         'action': 'decrease',
#     }
#     response = client.post(url, data=data)
#     shopping_cart_item = ShoppingCartItem.objects.last()

#     assert response.status_code == 302
#     assert shopping_cart_item.amount == amount


@pytest.mark.test_order_view
def test_order_view_order(db, client_user, item_factory, payment_method_factory, shopping_cart_item_factory, custom_user_factory):
    client, user = client_user
    seller = custom_user_factory.create()
    payment_methods = [payment_method_factory.create(method=method) for method in ['GadgetGrove', 'Card', 'Cash', 'Mail']]
    items = [item_factory.create(created_by=seller) for _ in range(4)]
    for item in items:
        shopping_cart_item_factory.create(user=user, item=item, amount=1)
    total_price = 1000
    total_amount = len(items)

    url = reverse('order:order', args=[seller.id, total_price, total_amount])
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.context['payment_methods']) == len(payment_methods)
    assert len(response.context['items']) == len(items)
    assert response.context['total_amount'] == total_amount
    assert response.context['total_price'] == total_price


@pytest.mark.test_order_view
@pytest.mark.parametrize(
    "street_address, city, state, postal_code, country, phone_number, first_name, last_name, email, order_comment, validity",
    [
        ("123 Test St", "Test City", "Test State", "12345", "Test Country", "0123456789", "TestFirstName", "TestLastName", "test@test.com", "Test comment", 302),
        ("123 Test St", "Test City", "Test State", "12345", "Test Country", "0123456789", "TestFirstName", "TestLastName", "test@test.com", "", 302),
        ("", "Test City", "Test State", "12345", "Test Country", "0123456789", "TestFirstName", "TestLastName", "test@test.com", "Test comment", 200),
        ("123 Test St", "", "Test State", "12345", "Test Country", "0123456789", "TestFirstName", "TestLastName", "test@test.com", "Test comment", 200),
        ("123 Test St", "Test City", "", "12345", "Test Country", "0123456789", "TestFirstName", "TestLastName", "test@test.com", "Test comment", 200),
        ("123 Test St", "Test City", "Test State", "", "Test Country", "0123456789", "TestFirstName", "TestLastName", "test@test.com", "Test comment", 200),
        ("123 Test St", "Test City", "Test State", "12345", "", "0123456789", "TestFirstName", "TestLastName", "test@test.com", "Test comment", 200),
        ("123 Test St", "Test City", "Test State", "12345", "Test Country", "", "TestFirstName", "TestLastName", "test@test.com", "Test comment", 200),
        ("123 Test St", "Test City", "Test State", "12345", "Test Country", "0123456789", "", "TestLastName", "test@test.com", "Test comment", 200),
        ("123 Test St", "Test City", "Test State", "12345", "Test Country", "0123456789", "TestFirstName", "", "test@test.com", "Test comment", 200),
        ("123 Test St", "Test City", "Test State", "12345", "Test Country", "0123456789", "TestFirstName", "TestLastName", "", "Test comment", 200),
    ]
)
def test_order_view_order_POST(db, 
                               client_user, 
                               item_factory, 
                               order_status_factory, 
                               payment_method_factory, 
                               shopping_cart_item_factory, 
                               custom_user_factory, 
                               street_address, 
                               city, 
                               state, 
                               postal_code, 
                               country, 
                               phone_number, 
                               first_name, 
                               last_name, 
                               email,
                               order_comment,
                               validity):
    client, user = client_user
    seller = custom_user_factory.create()
    for method in ['Card', 'Cash', 'Mail', 'GadgetPay']:
        payment_method_factory.create(method=method)
    for status in ['Checking', 'In progress', 'Done', 'Declined', 'Waiting']:
        order_status_factory.create(status=status)
    items = [item_factory.create(created_by=seller) for _ in range(4)]
    for item in items:
        shopping_cart_item_factory.create(user=user, item=item, amount=1)
    total_price = 1000
    total_amount = len(items)
    payment_method = "Cash"

    shipping_address_form_data = {
        'street_address': street_address,
        'city': city,
        'state': state,
        'postal_code': postal_code,
        'country': country,
    }

    contact_info_form_data = {
        'phone_number': phone_number,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
    }

    additional_data = {
        'selected_payment_method': payment_method,
        'order_comment': order_comment,
    }

    data = {**shipping_address_form_data, **contact_info_form_data, **additional_data}

    url = reverse('order:order', args=[seller.id, total_price, total_amount])
    response = client.post(url, data)

    assert response.status_code == validity