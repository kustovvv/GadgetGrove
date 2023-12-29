from pytest_factoryboy import register

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