from django.urls import path
from librarians import views

urlpatterns = [
    path('', views.home),
    path('create_borrowing', views.create_borrowing, name='create_borrowing'),
    path('return_borrowing', views.return_borrowing, name='return_borrowing'),
    path('display_medias', views.display_medias, name='display_medias'),
    path('add_media', views.add_media, name='add_media'),
    path('create_member', views.create_member, name='create_member'),
    path('display_members', views.display_members, name='display_members'),
    path('update_member', views.update_member, name='update_member'),
]
