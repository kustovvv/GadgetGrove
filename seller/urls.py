from django.urls import path
from . import views

app_name = 'seller'

urlpatterns = [
    path('seller_catalog/<int:seller_id>/', views.seller_catalog, name='seller_catalog'),
    path('seller_reviews/<int:seller_id>/', views.seller_reviews, name='seller_reviews'),
    path('seller_contacts/<int:seller_id>/', views.seller_contacts, name='seller_contacts'),
    path('seller_schedule/<int:seller_id>/', views.seller_schedule, name='seller_schedule'),
    path('seller_about/<int:seller_id>/', views.seller_about, name='seller_about'),
]