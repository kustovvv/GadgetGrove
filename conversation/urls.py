from django.urls import path
from . import views

app_name = 'conversation'

urlpatterns = [
    path('conversations/', views.conversations, name='conversations'),
    path('conversations/<str:pk>/', views.conversation, name='conversation'),
]