from . import views 
from django.urls import path

urlpatterns = [
    path('',views.home,name='picker-home'),
    path('login/',views.login,name='login'),
]