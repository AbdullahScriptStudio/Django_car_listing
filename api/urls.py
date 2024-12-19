from django.urls import path, include

from .views import get_view

urlpatterns = [
    path('api/', get_view, name = 'get_view')
]
