"""
URL configuration for bookmark project.

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
from django.urls import path,include #What does include do?
from django.contrib.auth import views as auth_view
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', auth_view.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout', views.custom_logout, name='logout'),
    path('', include('bookmarks2.urls'), namespace='bookmarks2')

]
