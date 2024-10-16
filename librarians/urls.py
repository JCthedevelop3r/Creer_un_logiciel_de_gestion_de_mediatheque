from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('create_loan', views.create_loan),
    path('return_loan', views.return_loan),
    path('display_medias', views.display_medias),
    path('add_media', views.add_media),
    path('create_member', views.create_member),
    path('display_members', views.display_members),
    path('update_member', views.update_member),
]
