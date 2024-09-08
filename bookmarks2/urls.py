from . import views
from django.urls import path
from . import views
from .models import Bookmark
from .views import HomeView
urlpatterns=[
    #path('', views.List.as_view(), name='List'),
    path('', HomeView.as_view(), name='home')
]