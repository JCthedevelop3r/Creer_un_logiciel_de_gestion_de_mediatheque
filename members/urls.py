from django.urls import path
from . import views

urlpatterns = [
    path('home_members', views.display_medias, name='display_medias' )