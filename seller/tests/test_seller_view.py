import pytest
from django.urls import reverse

@pytest.mark.test_seller_view
def test_seller_view_seller_catalog(db, client, custom_user_factory, category_brand_factory, item_factory, personal_information_factory, order_factory):
    seller = custom_user_factory.create()
    category_brand = category_brand_factory.create(category__name='Category 1')
    category_brand2 = category_brand_factory.create(category__name='Category 2')
    
    for _ in range(3):
        item_factory.create(category_brand=category_brand)
    items1 = [item_factory.create(created_by=seller, category_brand=category_brand) for _ in range(4)]
    items2 = [item_factory.create(created_by=seller, category_brand=category_brand2) for _ in range(2)]
    seller_info = personal_information_factory.create(user=seller)
    orders = [order_factory.create(seller=seller) for _ in range(3)]
        

    url = reverse('seller:seller_catalog', args=[seller.id])
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.context['items']) == len(items1)+len(items2)
    assert len(response.context['categories']) == 2
    assert response.context['seller_info'] == seller_info
    assert response.context['amount_orders'] == len(orders)

    data = {
        'category': category_brand2.category.id,
    }
    response = client.get(url, data=data)
    assert response.status_code == 200
    assert len(response.context['items']) == len(items2)


@pytest.mark.test_seller_view
def test_seller_view_seller_reviews(db, client, order_factory, personal_information_factory, custom_user_factory):
    seller = custom_user_factory.create()
    orders = [order_factory.create(seller=seller) for _ in range(3)]
    seller_info = personal_information_factory.create(user=seller)
    
    url = reverse('seller:seller_reviews', args=[seller.id])
    response = client.get(url)

    assert response.status_code == 200
    assert response.context['seller_info'] == seller_info
    assert response.context['amount_orders'] == len(orders)


@pytest.mark.test_seller_view
def test_seller_view_seller_contacts(db, client, order_factory, personal_information_factory, custom_user_factory):
    seller = custom_user_factory.create()
    orders = [order_factory.create(seller=seller) for _ in range(3)]
    seller_info = personal_information_factory.create(user=seller)
    
    url = reverse('seller:seller_contacts', args=[seller.id])
    response = client.get(url)

    assert response.status_code == 200
    assert response.context['seller_info'] == seller_info
    assert response.context['seller_additional_info'] is not None
    assert response.context['amount_orders'] == len(orders)


@pytest.mark.test_seller_view
def test_seller_view_seller_schedule(db, client, order_factory, personal_information_factory, custom_user_factory):
    seller = custom_user_factory.create()
    orders = [order_factory.create(seller=seller) for _ in range(3)]
    seller_info = personal_information_factory.create(user=seller)
    
    url = reverse('seller:seller_schedule', args=[seller.id])
    response = client.get(url)

    assert response.status_code == 200
    assert response.context['seller_info'] == seller_info
    assert response.context['amount_orders'] == len(orders)


@pytest.mark.test_seller_view
def test_seller_view_seller_about(db, client, order_factory, personal_information_factory, custom_user_factory):
    seller = custom_user_factory.create()
    orders = [order_factory.create(seller=seller) for _ in range(3)]
    seller_info = personal_information_factory.create(user=seller)
    
    url = reverse('seller:seller_about', args=[seller.id])
    response = client.get(url)

    assert response.status_code == 200
    assert response.context['seller_info'] == seller_info
    assert response.context['amount_orders'] == len(orders)

