from . import views
from django.urls import path

urlpatterns = [

    path('', views.home, name='home'),
    path('Approval', views.Approval, name='Approval'),
    path('temp', views.temp, name='temp'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
  ]