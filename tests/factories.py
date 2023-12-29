import factory
from faker import Faker
fake = Faker()

from item.models import Category, Brand, CategoryBrand, Item, Comments, FavoriteCompare
from order.models import ShippingAddress, ContactInfo, OrderStatus, PaymentMethod, Order, OrderItem, ShoppingCartItem, OrderReview
from conversation.models import Conversation, ConversationMessage
from authentication.models import User
from account.models import PersonalInformation

class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        skip_postgeneration_save=True

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', 'password')
    

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    
    name = factory.Sequence(lambda n: "category_slug_%d" % n)


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand
    
    name = factory.Sequence(lambda n: "brand_slug_%d" % n)


class CategoryBrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CategoryBrand

    category = factory.SubFactory(CategoryFactory)
    brand = factory.SubFactory(BrandFactory)


class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Item

    created_by = factory.SubFactory(CustomUserFactory)
    category_brand = factory.SubFactory(CategoryBrandFactory)
    model = factory.Sequence(lambda n: "item_id_%d" % n)
    description = fake.text()
    price = fake.pyfloat(right_digits=2, min_value=0.01, max_value=5000.00)
    availability = True
    image_url = "images/default.png"
    created_at = "2023-12-20 20:49:33"


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comments

    item = factory.SubFactory(ItemFactory)
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = factory.Faker('email')
    comment = fake.text()
    comment_date = "2023-12-20 20:49:33"


class FavoriteCompareFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FavoriteCompare
        skip_postgeneration_save = True

    user = factory.SubFactory(CustomUserFactory)
    
    @factory.post_generation
    def favorite_items(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        
        if extracted:
            for fav in extracted:
                self.favorite_items.add(fav)

    @factory.post_generation
    def compare_items(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        
        if extracted:
            for comp in extracted:
                self.compare_items.add(comp)


class ShippingAddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ShippingAddress

    street_address = fake.address()
    city = fake.city()
    state = fake.state()
    postal_code = fake.postalcode()
    country = fake.country()


class ContactInfoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ContactInfo
    phone_number = fake.phone_number()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()


class OrderStatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderStatus

    status = 'checking'


class PaymentMethodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PaymentMethod
    method = "card"


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    user = factory.SubFactory(CustomUserFactory)
    seller = factory.SubFactory(CustomUserFactory)
    contact_info = factory.SubFactory(ContactInfoFactory)
    status = factory.SubFactory(OrderStatusFactory)
    payment_method = factory.SubFactory(PaymentMethodFactory)
    shipping_address = factory.SubFactory(ShippingAddressFactory)
    order_date = "2023-12-20 20:49:33"
    total_price = fake.pyfloat(right_digits=2, min_value=0.01, max_value=5000.00)
    comment = fake.text()


class OrderItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderItem

    order = factory.SubFactory(OrderFactory)
    item = factory.SubFactory(ItemFactory)
    amount = fake.random_int(min=1, max=5)
    item_price = fake.pyfloat(right_digits=2, min_value=0.01, max_value=5000.00)


class ShoppingCartItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ShoppingCartItem

    user = factory.SubFactory(CustomUserFactory)
    item = factory.SubFactory(ItemFactory)
    amount = fake.random_int(min=1, max=100)


class OrderReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderReview

    order = factory.SubFactory(OrderFactory)
    comment = fake.text()
    comment_date = "2023-12-20 20:49:33"


class ConversationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Conversation
        skip_postgeneration_save = True

    item = factory.SubFactory(ItemFactory)
    created_by = factory.SubFactory(CustomUserFactory)
    created_at = "2023-12-20 20:49:33"
    modified_at = "2023-12-20 20:49:33"

    @factory.post_generation
    def conversation(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        
        if extracted:
            for conv in extracted:
                self.conversation.add(conv)
        

class ConversationMessageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ConversationMessage

    conversation = factory.SubFactory(ConversationFactory)
    created_by = factory.SubFactory(CustomUserFactory)
    content = fake.text()
    created_at = "2023-12-20 20:49:33"


class PersonalInformationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PersonalInformation

    user = factory.SubFactory(CustomUserFactory)
    avatar_url = "images/default.png"
    gender = "male"
    married = False
    have_children = False
    birthday = "2023-12-20"
    phone_number = fake.phone_number()
    facebook_url = f"facebook.com/{fake.first_name}_{fake.last_name}"
    instagram_url = f"instagram.com/{fake.first_name}_{fake.last_name}"
    twitter_url = f"twitter.com/{fake.first_name}_{fake.last_name}"
    google_url = f"plus.google.com/{fake.first_name}_{fake.last_name}"
    pinterest_url = f"pinterest.com/{fake.first_name}_{fake.last_name}"
    about = fake.text()
    hobby = fake.text()
    interests = fake.text()