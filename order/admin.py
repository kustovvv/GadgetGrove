from django.contrib import admin

from .models import Order, OrderItem, ShippingAddress, ContactInfo, Favorite

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(ContactInfo)
admin.site.register(Favorite)
