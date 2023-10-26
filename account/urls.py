from django.urls import path

from . import views

app_name='account'

urlpatterns = [
    path('history/', views.history, name='history'),
    path('<int:pk>/', views.order_details, name='order_details'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('comments/', views.account_comments, name='comments'),
    path('favorites/', views.favorites, name='favorites'),
    path('settings', views.settings, name='settings'),
]