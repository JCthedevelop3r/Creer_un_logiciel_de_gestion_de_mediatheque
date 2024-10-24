from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
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
    if request.method == 'POST':
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['e-mail']
        date_of_birth = request.POST['date-of-birth']
        place_of_birth = request.POST['place-of-birth']
        city_of_residence = request.POST['city-of-residence']
        phone_number = request.POST['phone-number']

        if User.objects.filter(email=email).exists():
            messages.error(request, "Un utilisateur avec cet e-mail existe déjà.")
            return render(request, 'librarians/create_member.html')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=f"{first_name} {last_name}"
        )

        member = Member.objects.create(
            user=user,
            date_of_birth=date_of_birth,
            place_of_birth=place_of_birth,
            city_of_residence=city_of_residence,
            phone_number=phone_number,
            borrowings_number=0
        )

        messages.success(request, "Le membre a été créé avec succès.")
        messages.error(request, "Une erreur s'est produite. Veuillez réessayer.")

    return render(request, 'librarians/create_member.html')


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
