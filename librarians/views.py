from django.shortcuts import render
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


def create_loan(request):
    context = {'name': 'create_loan'}
    return render(request, 'librarians/create_loan.html', context)


def return_loan(request):
    context = {'name': 'return_loan'}
    return render(request, 'librarians/return_loan.html', context)


def display_medias(request):
    context = {'name': 'display_medias'}
    return render(request, 'librarians/display_medias.html', context)


def add_media(request):
    context = {'name': 'add_media'}
    return render(request, 'librarians/add_media.html', context)


def create_member(request):
    context = {'name': 'create_member'}
    return render(request, 'librarians/create_member.html', context)


def display_members(request):
    context = {'name': 'display_members'}
    return render(request, 'librarians/display_members.html', context)


def update_member(request):
    context = {'name': 'update_member'}
    return render(request, 'librarians/update_member.html', context)
