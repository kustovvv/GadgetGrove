import pytest
from django.db import IntegrityError
from datetime import datetime


@pytest.mark.test_order_db
@pytest.mark.parametrize(
    "street_address, city, state, postal_code, country",
    [
        ('address 1 street 1', 'city1', 'state1', '12345', 'country1'),
        ('address 2 street 2', 'city2', 'state2', '21234', 'country2'),
        ('address 3 street 3', 'city3', 'state3', '12234', 'country3'),
    ]
)
def test_order_db_shipping_address_insert_data(db, shipping_address_factory, street_address, city, state, postal_code, country):
    """
    Test inserting a data into shipping_address model
    """
    new_shipping_address = shipping_address_factory.create(
        street_address=street_address, 
        city=city, 
        state=state, 
        postal_code=postal_code, 
        country=country
    )

    assert new_shipping_address.street_address == street_address
    assert new_shipping_address.city == city
    assert new_shipping_address.state == state
    assert new_shipping_address.postal_code == postal_code
    assert new_shipping_address.country == country


@pytest.mark.test_order_db
@pytest.mark.parametrize(
    "phone_number, first_name, last_name, email",
    [
        ("(123) 456-7890", "John", "Smith", "john.smith@gmail.com"),
        ("(555) 678-9012", "Mary", "Jones", "mary.jones@yahoo.com"),
        ("(789) 012-3456", "Peter", "Johnson", "peter.johnson@hotmail.com"),
    ]
)
def test_order_db_contact_info_insert_data(db, contact_info_factory, phone_number, first_name, last_name, email):
    """
    Test inserting a data into contact_info model
    """
    new_contact_info = contact_info_factory.create(
        phone_number=phone_number,
        first_name=first_name,
        last_name=last_name,
        email=email,
    )

    assert new_contact_info.phone_number == phone_number
    assert new_contact_info.first_name == first_name
    assert new_contact_info.last_name == last_name
    assert new_contact_info.email == email


@pytest.mark.test_order_db
@pytest.mark.parametrize(
    "status",
    [
        ("checking"),
        ("checking"),
        ("pending"),
    ]
)
def test_order_db_order_status_insert_data(db, order_status_factory, status):
    """
    Test inserting a data into order_status model
    """
    new_order_status = order_status_factory.create(status=status)

    assert new_order_status.status == status


@pytest.mark.test_order_db
def test_order_db_order_status_uniqueness_integrity(db, order_status_factory):
    """
    Test the uniqueness integrity on order_status model
    """
    order_status = order_status_factory.create()
    with pytest.raises(IntegrityError):
        order_status_factory.create(status=order_status.status)


@pytest.mark.test_order_db
@pytest.mark.parametrize(
    "method",
    [
        ("card"),
        ("cash"),
        ("mail"),
    ]
)
def test_order_db_payment_method_insert_data(db, payment_method_factory, method):
    """
    Test inserting a data into payment_method model
    """
    new_payment_method = payment_method_factory.create(method=method)

    assert new_payment_method.method == method


@pytest.mark.test_order_db
def test_order_db_payment_method_uniqueness_integrity(db, payment_method_factory):
    """
    Test the uniqueness integrity on payment_method model
    """
    payment_method = payment_method_factory.create()
    with pytest.raises(IntegrityError):
        payment_method_factory.create(method=payment_method.method)


@pytest.mark.test_order_db
@pytest.mark.parametrize(
    "total_price, comment",
    [
        ('100.00', 'no comment'),
        ('200.00', 'special instructions'),
        ('300.00', 'gift'),
    ]
)
def test_order_db_order_insert_data(db, order_factory, total_price, comment):
    """
    Test inserting a data into order model
    """
    new_order = order_factory.create(total_price=total_price, comment=comment)

    assert new_order.user is not None
    assert new_order.seller is not None
    assert new_order.contact_info is not None
    assert new_order.status is not None
    assert new_order.payment_method is not None
    assert new_order.shipping_address is not None
    assert new_order.order_date is not None
    assert new_order.total_price == total_price
    assert new_order.comment == comment


@pytest.mark.test_order_db
@pytest.mark.parametrize(
    "amount, item_price",
    [
        ('2', '234.12'),
        ('1', '10.10'),
        ('4', '2222.99'),
    ]
)
def test_order_db_order_item_insert_data(db, order_item_factory, amount, item_price):
    """
    Test inserting a data into order_item model
    """
    new_order_item = order_item_factory.create(amount=amount, item_price=item_price)
    
    assert new_order_item.order is not None
    assert new_order_item.item is not None
    assert new_order_item.amount == amount
    assert new_order_item.item_price == item_price


@pytest.mark.test_order_db
def test_order_db_shopping_cart_item_insert_data(db, shopping_cart_item_factory):
    """
    Test inserting a data into shopping_cart_item model
    """
    new_shopping_cart_item = shopping_cart_item_factory.create()

    assert new_shopping_cart_item.user is not None
    assert new_shopping_cart_item.item is not None
    assert new_shopping_cart_item.amount is not None


@pytest.mark.test_order_db
@pytest.mark.parametrize(
    "rating, comment",
    [
        ("1", "comment"),
        ("5", "nothing"),
        ("3", "text"),
    ]
)
def test_order_db_order_review_insert_data(db, order_review_factory, rating, comment):
    """
    Test inserting a data into order_review model
    """
    new_order_review = order_review_factory.create(rating=rating, comment=comment)

    assert new_order_review.comment_date is not None
    assert new_order_review.rating == rating
    assert new_order_review.comment == comment