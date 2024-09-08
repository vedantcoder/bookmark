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
from django.views.generic import ListView
from django.urls import path,include #What does include do?
from django.contrib.auth import views as auth_view
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import path
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone
from taggit.managers import TaggableManager
import requests
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name Here'})))
    last_name = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name Here'})))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'Auth/register.html'
    success_url = reverse_lazy('login')

from django.contrib.auth.models import User
from django import forms


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', auth_view.LoginView.as_view(template_name='Auth/login.html'), name='login'),
    path('logout', custom_logout, name='logout'),
    path('register/', UserRegisterView.as_view(template_name='Auth/register.html'), name='register'),
    #path('bookmarks', include('bookmarks2.urls'), name='bookmarks2')
    path('', include('bookmarks2.urls')),
]


