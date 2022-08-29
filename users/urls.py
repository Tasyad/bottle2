from django.urls import path
from . import views
from .views import register, profile, user_detail
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
    path('delete_user<int:pk>/', views.DeleteUser.as_view(), name='delete_user'),
    path('detail/<int:pk>', user_detail, name='users-detail'),
]


