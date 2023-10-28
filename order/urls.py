from django.urls import path

from . import views

app_name = 'order'

urlpatterns = [
    path('<int:pk>/<int:amount>/', views.add_to_cart, name='add_to_cart'),
    path('<int:pk>/', views.delete_from_cart, name='delete_from_cart'),
    path('change/<int:pk>/', views.change_amount_items, name='change_amount_items'),
    path('order/', views.order, name='order'),
    path('add_delete_favorites/<int:pk>/', views.add_delete_favorites, name='add_delete_favorites'),
]