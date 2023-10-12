from django.contrib import admin

from .models import Order, OrderItem, ShippingAddress, ContactInfo

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(ContactInfo)