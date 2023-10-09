from django.urls import path

from . import views

app_name = 'order'

urlpatterns = [
    path('<int:pk>/<int:amount>/', views.add_to_cart, name='add_to_cart'),
    path('<int:pk>/', views.delete_from_cart, name='delete_from_cart'),
    # path('toggle_navbar/', views.toggle_navbar, name='toggle_navbar'),
]