from django.urls import path
from .views import SignupView, HomeView, AboutView, NewsView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('haqida/', AboutView.as_view(), name='haqida'),
    path('news/', NewsView.as_view(), name='news'),


]