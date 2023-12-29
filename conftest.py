import pytest
from django.test import Client
from pytest_factoryboy import register

from authentication.models import User

from tests.factories import CategoryFactory, BrandFactory, CategoryBrandFactory, CustomUserFactory, ItemFactory, CommentFactory, FavoriteCompareFactory,\
    ShippingAddressFactory, ContactInfoFactory, OrderStatusFactory, PaymentMethodFactory, OrderFactory, OrderItemFactory, ShoppingCartItemFactory, OrderReviewFactory,\
    ConversationFactory, ConversationMessageFactory,\
    PersonalInformationFactory
    

pytest_plugins = [
    "tests.fixtures",
    "tests.selenium",
]

#Account factories
register(CustomUserFactory)

#Authentication factories
register(PersonalInformationFactory)

#Item factories
register(CategoryFactory)
register(BrandFactory)
register(CategoryBrandFactory)
register(ItemFactory)
register(CommentFactory)
register(FavoriteCompareFactory)

#Order factories
register(ShippingAddressFactory)
register(ContactInfoFactory)
register(OrderStatusFactory)
register(PaymentMethodFactory)
register(OrderFactory)
register(OrderItemFactory)
register(ShoppingCartItemFactory)
register(OrderReviewFactory)

#Conversation factories
register(ConversationFactory)
register(ConversationMessageFactory)

@pytest.fixture
def client(db):
    client = Client()
    user = User.objects.create_user(username='test_user', password='password')
    client.force_login(user)
    return client

@pytest.fixture
def client_user(db):
    client = Client()
    user = User.objects.create(username='test_user', password='password')
    client.force_login(user)
    return client, user