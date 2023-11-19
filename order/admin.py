from django.contrib import admin

from .models import ShippingAddress, ContactInfo, OrderStatus, PaymentMethod, Order, OrderItem, OrderReview

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(ContactInfo)
admin.site.register(OrderStatus)
admin.site.register(PaymentMethod)
admin.site.register(OrderReview)