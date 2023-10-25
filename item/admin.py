from django.contrib import admin

from .models import Item, Brand, Category, Comments

admin.site.register(Item)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Comments)