from datetime import date, timedelta
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from itertools import chain
from .models_borrowing import Borrowing
from .models_members import Member
from .models_medias import Book, Cd, Board_game, Dvd


# Create your views here.
def home(request):
    members_list = Member.objects.all()
    medias_list = chain(Book.objects.all() + Cd.objects.all() + Board_game.objects.all() + Dvd.objects.all())
    context = {
        'name': 'home',
        'members_list': members_list,
        'medias_list': medias_list
    }
    return render(request, 'librarians/home.html', context)


def create_borrowing(request):
    if request.method == 'POST':
        member_id = request.POST.get('member_id')
        media_ids = request.POST.getlist('media_ids')

        member = get_object_or_404(Member, id=member_id)

        # Récupération des emprunts en cours du membre
        current_borrowings = Borrowing.objects.filter(member=member)

        # Vérification si l'un des emprunts en cours a dépassé la date d'échéance
        # Récupère les emprunts dont la "due_date" est inférieure à la date d'aujourd'hui
        has_overdue_borrowing = current_borrowings.filter(due_date__lt=timezone.now().date()).exists()

        if current_borrowings.count() >= 3:
            messages.error(request, "Ce membre a déjà atteint le nombre maximum d'emprunts (3).")
            return redirect('create_borrowing')

        if has_overdue_borrowing:
            messages.error(request,
                           "Ce membre a au moins un emprunt en retard et ne peut pas emprunter de nouveaux médias.")
            return redirect('create_borrowing')

        # Recherche du média sélectionné en fonction de son id en parcourant chaque type de média
        for media_id in media_ids:
            media = None
            for model in (Book, Cd, Board_game, Dvd):
                try:
                    media = model.objects.get(id=media_id)
                    break
                except model.DoesNotExist:
                    continue

            if media:
                Borrowing.objects.create(member=member, media=media)

        messages.success(request, "L'emprunt a été créé avec succès.")
        return redirect('create_borrowing')

    members_list = Member.objects.all()
    context = {
        'name': 'create_borrowing',
        'members_list': members_list,
        'books_list': Book.objects.all(),
        'cds_list': Cd.objects.all(),
        'board_games_list': Board_game.objects.all(),
        'dvds_list': Dvd.objects.all(),
    }
    return render(request, 'librarians/create_borrowing.html', context)


def return_borrowing(request):
    borrowings_list = Borrowing.objects.all()
    members_list = Member.objects.all()
    medias_list = chain(Book.objects.all() + Cd.objects.all() + Board_game.objects.all() + Dvd.objects.all())
    context = {
        'name': 'return_borrowing',
        'members_list': members_list,
        'medias_list': medias_list,
        'borrowings_list': borrowings_list
    }
    return render(request, 'librarians/return_borrowing.html', context)


def display_medias(request):
    if request.method == 'POST':
        media_id = request.POST.get("media-id")
        media_type = request.POST.get("media-type")

        media = None
        if media_type == "book":
            media = get_object_or_404(Book, id=media_id)
        elif media_type == "cd":
            media = get_object_or_404(Cd, id=media_id)
        elif media_type == "board_game":
            media = get_object_or_404(Board_game, id=media_id)
        elif media_type == "dvd":
            media = get_object_or_404(Dvd, id=media_id)

        if media:
            media.delete()
            messages.success(request, "Le média a été supprimé avec succès.")

    context = {
        'name': 'display_medias',
        'books_list': Book.objects.all(),
        'cds_list': Cd.objects.all(),
        'board_games_list': Board_game.objects.all(),
        'dvds_list': Dvd.objects.all(),
    }
    return render(request, 'librarians/display_medias.html', context)


def add_media(request):
    if request.method == 'POST':
        media_name = request.POST['media-name']
        media_type = request.POST['media-type']
        media_quantity = request.POST['media-quantity']

        if Media.objects.filter(name=media_name, type=media_type).exists():
            messages.error(request, "Ce média a déjà été ajouté.")
            return render(request, 'librarians/add_media.html', {
                'media_name': media_name,
                'media_type': media_type,
                'media_quantity': media_quantity
            })

        if media_type == "Livre":
            media_author = request.POST.get('media-author')
            book = Media.objects.create(
                name=media_name,
                author= media_author,
                type=media_type,
                quantity=int(media_quantity)
            )
        elif media_type == "CD":
            media_artist = request.POST.get('media-artist')
            cd = Media.objects.create(
                name=media_name,
                artist= media_artist,
                type=media_type,
                quantity=int(media_quantity)
            )
        elif media_type == "Jeu de plateau":
            media_creator = request.POST.get('media-creator')
            board_game = Media.objects.create(
                name=media_name,
                creator= media_creator,
                type=media_type,
                quantity=int(media_quantity)
            )
        else:
            media_director = request.POST.get('media-director')
            dvd = Media.objects.create(
                name=media_name,
                director= media_director,
                type=media_type,
                quantity=int(media_quantity)
            )

        messages.success(request, "Le média a été ajouté avec succès.")

    return render(request, 'librarians/add_media.html')


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
    return render(request, 'librarians/create_member.html')


def display_members(request):
    if request.method == 'POST':
        member_id = request.POST.get("member-id")
        member = get_object_or_404(Member, id=member_id)
        user = member.user
        user.delete()
        member.delete()
        messages.success(request, "Le membre a été supprimé avec succès.")

    members_list = Member.objects.all()
    context = {
        'name': 'display_members',
        'members_list': members_list
    }
    return render(request, 'librarians/display_members.html', context)


def update_member(request):
    context = {'name': 'update_member'}
    return render(request, 'librarians/update_member.html', context)
