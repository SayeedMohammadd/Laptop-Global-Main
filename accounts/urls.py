from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('user/<username>', views.user_profile, name='profile'),
    path('user/<username>/ads', views.userads, name='userads'),
]
