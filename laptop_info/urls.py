"""
URL configuration for laptop_info project.

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
from django.urls import path,include
import apple,hp,dell
from apple.views import *
from hp.views import *
from dell.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('apple/',include('apple.urls')),
    path('first/',first,name='fisrt'),
    path('second/',second,name='second'),
    path('hp/',include('hp.urls')),
    path('third/',third,name='third'),
    path('dell/',include('dell.urls')),

]
