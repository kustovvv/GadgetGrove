from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path('<int:pk>/', views.details, name='details'),
    path('', views.items, name='items'),
    path('comments/<int:pk>/', views.comments, name='comments'),
    path('favorites/', views.favorites, name='favorites'),
    path('add_delete_favorites_compare/<int:pk>/', views.add_delete_favorites_compare, name='add_delete_favorites_compare'),
    path('compare/', views.compare, name='compare'),
    path('add_update_item/', views.add_update_item, name='add_update_item'),
    path('delete_item/<int:pk>/', views.delete_item, name='delete_item'),
    path('delete_items/', views.delete_items, name='delete_items'),
]