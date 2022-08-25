from django.urls import path
from .views import register, profile, delete
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(
                                                    template_name='users/login.html',
                                                ), name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(
                                                    template_name='blog/home.html',
    ), name='logout'),
    path('profile/', profile, name='profile'),
]


