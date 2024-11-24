from django.urls import path
from members import views

urlpatterns = [
    path('', views.home_members, name='home_members' )
]