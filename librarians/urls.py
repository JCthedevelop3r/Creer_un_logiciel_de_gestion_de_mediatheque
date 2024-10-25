from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('create_borrowing', views.create_borrowing, name='create_borrowing'),
    path('return_borrowing', views.return_borrowing),
    path('display_medias', views.display_medias),
    path('add_media', views.add_media),
    path('create_member', views.create_member),
    path('display_members', views.display_members),
    path('update_member', views.update_member),
]
