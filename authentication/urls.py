from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'authentication'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html'), name='login'),
]