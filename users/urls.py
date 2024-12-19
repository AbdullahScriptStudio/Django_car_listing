from django.urls import path 
from .views import login_page, register_page, Register


urlpatterns = [
    path('login/',login_page, name = 'login' ),
    path('register/', Register.as_view(), name = 'register')
]
