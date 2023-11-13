from django.urls import path

from . import views

app_name='account'

urlpatterns = [
    path('history/', views.history, name='history'),
    path('<int:pk>/', views.order_details, name='order_details'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('comments/', views.account_comments, name='comments'),
    path('settings', views.settings, name='settings'),
    path('card/', views.card, name='card'),
    path('conversations/', views.conversations, name='conversations'),
    path('discounts/', views.discounts, name='discounts'),
    path('ads/', views.ads, name='ads'),
]