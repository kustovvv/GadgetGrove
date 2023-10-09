from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('items/', include('item.urls')),
    path('orders/', include('order.urls')),
]
