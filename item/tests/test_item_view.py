import pytest
from django.urls import reverse
from django.test import Client
from django.core.files.uploadedfile import SimpleUploadedFile

from item.models import Item, Category, Brand, CategoryBrand, Comments, FavoriteCompare
from authentication.models import User


@pytest.mark.test_item_view
def test_item_view_add_update_item(db):
    client = Client()
    response = client.get(f"/items/add_update_item/")

    assert response.status_code == 302


@pytest.mark.test_item_view
def test_item_view_add_update_item_GET(db, client):
    response = client.get(reverse('item:add_update_item'))

    assert response.status_code == 200
    assert response.context['item'] == ''
    assert response.context['item_id'] == ''
    assert response.context['selected_category'] == -1
    assert response.context['selected_brand'] == ''
    assert response.context['all_categories'].exists
    assert response.context['brands'].exists


@pytest.mark.test_item_view
@pytest.mark.parametrize(
    "title, price, category, brand, is_available, image_url, description, validity", 
    [
        ("Smartphone", 699.99, "1", "1", True, "smartphone_image.jpg", "A powerful smartphone with advanced features.", True),
        ("Wireless Earbuds", 89.99, "1", "2", False, "earbuds_image.jpg", "High-quality wireless earbuds for a seamless audio experience.", True),
        ("Wireless Earbuds", 89.99, "1", "2", False, '', "High-quality wireless earbuds for a seamless audio experience.", True),
        ("Wireless Earbuds", 89.99, "1", "2", False, "earbuds_image.jpg", '', True),
        ("Laptop", "s", "10", "3", True, "laptop_image.jpg", "A reliable laptop with excellent performance and long battery life.", False),
        ("Laptop", 29.99, '', "3", True, "laptop_image.jpg", "A reliable laptop with excellent performance and long battery life.", False),
        ("Laptop", 29.99, "10", '', True, "laptop_image.jpg", "A reliable laptop with excellent performance and long battery life.", False),
    ]
)
def test_item_view_add_update_item_POST(db, client, title, price, category, brand, is_available, image_url, description, validity):
    if category:
        category_obj = Category.objects.create(id=category, name='Test Category')
    if brand:
        brand_obj = Brand.objects.create(id=brand, name='Test Brand')
    if category and brand:
        category_brand = CategoryBrand.objects.create(category=category_obj, brand=brand_obj)
    if image_url:
        image_url = SimpleUploadedFile(image_url, b'file_content', content_type='image/jpeg')
    data = {
        'new_title_input': title,
        'new_price_input': price,
        'category-select-item': category,
        'brand-select': brand,
        'is_available': is_available,
        'new_image': image_url,
        'new_description_input': description,
    }

    response = client.post(reverse('item:add_update_item'), data=data)
    item = Item.objects.last()

    assert response.status_code == 302
    assert Item.objects.count() == validity
    if Item.objects.count():
        assert item.model == title
        assert item.category_brand == category_brand
        assert item.description == description
        assert item.price == price
        if item.image_url:
            assert item.image_url.name.startswith('item_images/' + image_url.name.rsplit('.', 1)[0])
        assert item.availability == is_available


@pytest.mark.test_item_view
def test_item_view_delete_item(db, client, item_factory):
    item = item_factory.create()
    assert Item.objects.count() == 1
    url = reverse('item:delete_item', args=[item.id])
    response = client.post(url, follow=True)
    
    assert response.status_code == 200
    assert Item.objects.count() == 0


@pytest.mark.test_item_view
def test_item_view_delete_items(db, client, item_factory, custom_user_factory):
    items = [item_factory.create() for _ in range(3)]
    assert Item.objects.count() == 3
    selectedValues = ', '.join(list(str(item.id) for item in Item.objects.all()))

    url = reverse('item:delete_items')
    data = {
        'selectedValues': selectedValues,
    }
    response = client.get(url, data=data, follow=True)

    assert response.status_code == 200
    assert Item.objects.count() == 0


@pytest.mark.test_item_view
def test_item_view_details(db, client, item_factory, comment_factory):
    new_item = item_factory.create()
    
    for _ in range(3):
        item_factory.create(category_brand=new_item.category_brand)
        comment_factory.create(item=new_item)
    
    response = client.get(f"/items/{new_item.id}/")

    assert response.status_code == 200
    assert response.context['item'] == new_item
    assert response.context['item'].model == new_item.model
    assert response.context['item'].description == new_item.description
    assert response.context['item'].price == new_item.price
    assert response.context['item'].availability == new_item.availability
    assert response.context['item'].image_url == new_item.image_url
    assert response.context['item'].category_brand.category.name == new_item.category_brand.category.name
    assert response.context['item'].category_brand.brand.name == new_item.category_brand.brand.name
    assert len(response.context['related_items']) == 3
    assert len(response.context['comments']) == 3


@pytest.mark.test_item_view
def test_item_view_items(db, client_user, item_factory, category_brand_factory):
    client, user = client_user
    category_brand = category_brand_factory.create()
    for _ in range(2):
        item_factory.create(created_by=user, category_brand=category_brand)
    for _ in range(3):
        item_factory.create()
    for _ in range(4):
        item_factory.create(category_brand=category_brand) 

    assert Item.objects.count() == 9

    item = Item.objects.last()
    category = item.category_brand.category.id
    brand = item.category_brand.brand.id
    data = {
        'category': category,
        'brand': brand,
    }

    url = reverse('item:items')
    response = client.get(url, data=data, follow=True)

    assert response.status_code == 200
    assert len(response.context['items']) == 4


@pytest.mark.test_item_view
def test_item_view_comments(db, client, item_factory, comment_factory):
    item = item_factory.create()
    comment_factory.create()
    for _ in range(4):
        comment_factory.create(item=item)

    assert Comments.objects.count() == 5

    url = reverse('item:comments', args=[item.id])
    response = client.get(url)

    assert response.status_code == 200
    assert response.context['item'] == item
    assert len(response.context['comments']) == 4


@pytest.mark.test_item_view
def test_item_view_favorites(db, client_user, item_factory, favorite_compare_factory, category_factory, brand_factory, category_brand_factory):
    client, user = client_user
    user2 = User.objects.create(username='test_user2', password='password', email='test@test.com')

    category = category_factory(name='Test category')
    brand = brand_factory(name='Test brand')
    category_brand = category_brand_factory(category=category, brand=brand)
    
    items = [item_factory.create(created_by=user2, category_brand=category_brand) for _ in range(4)]
    items.append(item_factory.create(created_by=user2, category_brand=category_brand, availability=False))
    items.append(item_factory.create(category_brand=category_brand))
    items.append(item_factory.create())
    favorite_compare_factory(user=user, favorite_items=items)
    
    url = reverse('item:favorites')
    response = client.get(url)
    
    assert Item.objects.count() == 7
    assert response.status_code == 200
    assert len(response.context['items']) == 7
    assert len(response.context['all_categories']) == 2
    assert len(response.context['all_sellers']) == 3

    datasets = [
        {'category': str(category.id), 'seller': user2, 'is_available': 'true', 'item_amount': 4},
        {'category': str(category.id), 'seller': user2, 'item_amount': 5},
        {'is_available': 'true', 'item_amount': 6},
        {'category': str(category.id), 'item_amount': 6},
        {'seller': user2,'item_amount': 5},
    ]    
    for data in datasets:
        response = client.get(url, data=data)
        assert response.status_code == 200
        assert len(response.context['items']) == data['item_amount']
        

@pytest.mark.test_item_view
def test_item_view_add_delete_favorites_compare(db, client, item_factory):
    item = item_factory.create()
    
    data = {
        'model_option': 'favorites',
    }

    url = reverse('item:add_delete_favorites_compare', args=[item.id])
    response = client.get(url, data)

    favorite_compare_items = FavoriteCompare.objects.last()
    favorite_items = favorite_compare_items.favorite_items
    compare_items = favorite_compare_items.compare_items

    assert response.status_code == 302
    assert FavoriteCompare.objects.count() == 1
    assert favorite_items.count() == 1
    assert favorite_items.last() == item

    response = client.get(url)
    assert response.status_code == 302
    assert FavoriteCompare.objects.count() == 1
    assert compare_items.count() == 1
    assert compare_items.last() == item


@pytest.mark.test_item_view
def test_item_view_compare(db, client_user, item_factory, category_factory, category_brand_factory, favorite_compare_factory):
    client, user = client_user
    category = category_factory.create(name="First category")
    category2 = category_factory.create(name='Second category')
    category_brand = category_brand_factory.create(category=category)
    category_brand2 = category_brand_factory.create(category=category2)
    items = [item_factory.create(category_brand=category_brand) for _ in range(4)]
    items.append(item_factory.create(category_brand=category_brand2))
    favorite_compare_factory.create(user=user, compare_items=items)

    url = reverse('item:compare')
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.context['items']) == 5
    assert len(response.context['categories']) == 2

    selected_category = category.id

    data = {
        'selected_category': selected_category,
    }

    response = client.get(url, data=data)

    assert response.status_code == 200
    assert response.context['selected_category'] == selected_category
    assert len(response.context['items']) == 4