"""
URL configuration for automax project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import urls as home_urls
from django.conf.urls.static import static
from django.conf import settings
from users import urls as users_url
from api import urls as api_url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_urls)),
    path('home', include(home_urls)),
    path('', include(users_url)),
    path('', include(api_url)),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)