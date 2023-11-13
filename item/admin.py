from django.contrib import admin

from .models import Brand, Category, CategoryBrand, FavoriteCompare, Comments, Item

admin.site.register(Item)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(CategoryBrand)
admin.site.register(FavoriteCompare)