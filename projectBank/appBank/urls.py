from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name='home'),
    path('register',views.register, name='register'),
    path('reglogin',views.reglogin, name='reglogin'),
    path('user_login',views.user_login, name='user_login'),
    path('user_logout',views.user_logout, name='user_logout'),
    path('cm_register',views.cm_register, name='cm_register'),
]
