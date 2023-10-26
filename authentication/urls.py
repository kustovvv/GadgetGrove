from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', views.user_login, name='login'),
    path('activate-user/<uidb64>/<token>', views.activate_user, name='activate'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='authentication/reset_password.html'), 
         name='reset_password'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="authentication/reset_password_sent.html"), 
        name="password_reset_done"),    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="authentication/reset.html"), 
         name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="authentication/reset_password_complete.html"), 
         name='password_reset_complete'),
]