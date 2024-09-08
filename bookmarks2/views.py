from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Bookmark
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import Bookmark

#class List(LoginRequiredMixin, generic.ListView):
    #model = models.Bookmark

    #def get_queryset(self):
        #return self.request.user.bookmarks2.all()

class HomeView(ListView):
    model = Bookmark
    template_name = 'layouts/home.html'