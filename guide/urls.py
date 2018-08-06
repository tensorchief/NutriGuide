from django.urls import path
from django.contrib.auth.views import auth_login

from guide import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
]
