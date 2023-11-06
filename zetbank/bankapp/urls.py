from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('register/register', views.register, name='register'),
    path('login/login', views.login, name='login'),
    path('new/', views.new, name='new'),
    path('form/',views.form,name='form'),
    path('success/',views.success,name='success'),
    path('logout/',views.logout,name='logout'),
    path('a/',views.a,name='a'),
    ]