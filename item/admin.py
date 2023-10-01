from django.contrib import admin

from .models import Item, Brand, Category

admin.site.register(Item)
admin.site.register(Brand)
admin.site.register(Category)