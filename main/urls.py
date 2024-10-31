from django.contrib.auth import views as auth_views    
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.login_view, name = 'login'),
    path('login/', views.login_view, name = 'login'),
    path('signup/', views.signup_view, name = 'signup'),
    path('forgot-password/', auth_views.PasswordResetView.as_view(template_name= "forgot_password.html"),
          name = "forgot_password"),
    path('change-password/', views.cpass_view, name = 'change_pass'),
    path('dashboard/', views.dash_view, name = 'dashboard'),
    path('profile/', views.profile_view, name = 'profile'),
    path('logout/', views.logout_view, name = 'logout'),
   
    path('forgot-password-done/', auth_views.PasswordResetDoneView.as_view(template_name="email_sent_confirm.html"),
          name = "password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset_pass.html"),
         name = "password_reset_confirm"),
    path('forgot-password-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
         name = "password_reset_complete"),
]