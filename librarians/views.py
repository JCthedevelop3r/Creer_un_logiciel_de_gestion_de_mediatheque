from django.shortcuts import render

from .models_borrowing import Borrowing
from .models_members import Member
from .models_medias import Media


# Create your views here.
def home(request):
    members_list = Member.objects.all()
    medias_list = Media.objects.all()
    context = {
        'name': 'home',
        'members_list': members_list,
        'medias_list': medias_list
    }
    return render(request, 'librarians/home.html', context)


def create_borrow(request):
    members_list = Member.objects.all()
    medias_list = Media.objects.all()
    context = {
        'name': 'create_borrow',
        'members_list': members_list,
        'medias_list': medias_list
    }
    return render(request, 'librarians/create_borrow.html', context)


def return_borrowing(request):
    borrowings_list = Borrowing.objects.all()
    members_list = Member.objects.all()
    medias_list = Media.objects.all()
    context = {
        'name': 'return_borrowing',
        'members_list': members_list,
        'medias_list': medias_list,
        'borrowings_list': borrowings_list
    }
    return render(request, 'librarians/return_borrowing.html', context)


def display_medias(request):
    medias_list = Media.objects.all()
    context = {
        'name': 'display_medias',
        'medias_list': medias_list
    }
    return render(request, 'librarians/display_medias.html', context)


def add_media(request):
    context = {'name': 'add_media'}
    return render(request, 'librarians/add_media.html', context)


def create_member(request):
    context = {'name': 'create_member'}
    return render(request, 'librarians/create_member.html', context)


def display_members(request):
    members_list = Member.objects.all()
    context = {
        'name': 'display_members',
        'members_list': members_list
    }
    return render(request, 'librarians/display_members.html', context)


def update_member(request):
    context = {'name': 'update_member'}
    return render(request, 'librarians/update_member.html', context)
