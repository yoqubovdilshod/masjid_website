from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.views import TemplateView
from django.shortcuts import HttpResponse, render

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'haqida.html'

class NewsView(TemplateView):
    template_name = 'news.html'



    
