from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('items/', include('item.urls')),
    path('orders/', include('order.urls')),
    path('seller/', include('seller.urls')),
    path('account/', include('account.urls')),
    path('conversation/', include('conversation.urls')),
    path('authentication/', include('authentication.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
