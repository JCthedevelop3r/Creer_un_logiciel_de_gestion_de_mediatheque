from datetime import timedelta
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from itertools import chain
from django.contrib.contenttypes.models import ContentType
from .models_borrowing import Borrowing
from .models_members import Member
from .models_medias import Book, Cd, Board_game, Dvd, Media
from django.utils.timezone import now


def home(request):
    members_list = Member.objects.all()
    medias_list = chain(Book.objects.all(), Cd.objects.all(), Board_game.objects.all(), Dvd.objects.all())
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

        all_media = {
            **{book.id: book for book in Book.objects.all()},
            **{cd.id: cd for cd in Cd.objects.all()},
            **{board_game.id: board_game for board_game in Board_game.objects.all()},
            **{dvd.id: dvd for dvd in Dvd.objects.all()},
        }

        for media_id in media_ids:
            media = all_media.get(int(media_id))
            if media:
                content_type = ContentType.objects.get_for_model(media)
                if media.quantity > 0:
                    Borrowing.objects.create(
                        member=member,
                        content_type=content_type,
                        object_id=media.id,
                        due_date = timezone.now().date() + timedelta(days=7)
                    )
                    media.quantity -= 1
                    media.save()
                    member.borrowings_number += 1
                    member.save()
                else:
                    messages.error(request, f"Le média {media.name} ({content_type}) n'est pas disponible.")
            else:
                messages.error(request, f"Le média avec l'id {media_id} est introuvable.")

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
    if request.method == 'POST':
        borrowing_ids = request.POST.getlist('borrowing_ids')

        for borrowing_id in borrowing_ids:
            borrowing = get_object_or_404(Borrowing, id=borrowing_id)
            member_id = request.POST.get(f'member_id_{borrowing_id}')
            member = get_object_or_404(Member, id=member_id)
            media = borrowing.media

            if media:
                member.borrowings_number -= 1
                member.save()

                media.quantity += 1
                media.save()

                media.media_unavailable()
                borrowing.delete()

                messages.success(request, "Les emprunts ont été rentrés avec succès.")
                return redirect('return_borrowing')

    borrowings_list = Borrowing.objects.all()
    for borrowing in borrowings_list:
        borrowing.is_overdue = borrowing.due_date < now().date()

    members_list = Member.objects.all()
    medias_list = chain(Book.objects.all(), Cd.objects.all(), Board_game.objects.all(), Dvd.objects.all())

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

        print("Media ID :", media_id)
        print("Media Type :", media_type)

        media = None
        if media_type == "book":
            media = get_object_or_404(Book, id=media_id)
        elif media_type == "cd":
            media = get_object_or_404(Cd, id=media_id)
        elif media_type == "board_game":
            media = get_object_or_404(Board_game, id=media_id)
        elif media_type == "dvd":
            media = get_object_or_404(Dvd, id=media_id)

        print("Media trouvé :", media)

        if media:
            media.delete()
            messages.success(request, "Le média a été supprimé avec succès.")
            print("Message de succès ajouté.")
        else:
            print("Aucun média trouvé.")

    medias_list = chain(Book.objects.all(), Cd.objects.all(), Board_game.objects.all(), Dvd.objects.all())

    context = {
        'name': 'display_medias',
        'medias_list': medias_list,
    }
    return render(request, 'librarians/display_medias.html', context)


def add_media(request):
    if request.method == 'POST':
        media_name = request.POST['media-name']
        media_type = request.POST['media-type']
        media_creator = request.POST['media-creator']
        media_quantity = request.POST['media-quantity']

        if Book.objects.filter(name=media_name, type=media_type, author=media_creator).exists() or Cd.objects.filter(
                name=media_name, type=media_type, artist=media_creator).exists() or Board_game.objects.filter(
            name=media_name, type=media_type, creator=media_creator).exists() or Dvd.objects.filter(name=media_name,
                                                                                                    type=media_type,
                                                                                                    director=media_creator).exists():
            messages.error(request, "Ce média a déjà été ajouté.")
            return render(request, 'librarians/add_media.html', {
                'media_name': media_name,
                'media_type': media_type,
                'media_quantity': media_quantity
            })

        if media_type == "book":
            Book.objects.create(
                name=media_name,
                author=media_creator,
                type=media_type,
                quantity=int(media_quantity)
            )
        elif media_type == "cd":
            Cd.objects.create(
                name=media_name,
                artist=media_creator,
                type=media_type,
                quantity=int(media_quantity)
            )
        elif media_type == "board_game":
            Board_game.objects.create(
                name=media_name,
                creator=media_creator,
                type=media_type,
                quantity=int(media_quantity)
            )
        else:
            Dvd.objects.create(
                name=media_name,
                director=media_creator,
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
    if request.method == 'POST':
        member_id = request.POST.get("member-id")
        member = get_object_or_404(Member, id=member_id)

        member.user.first_name = request.POST.get('first-name')
        member.user.last_name = request.POST.get('last-name')
        member.user.email = request.POST.get('e-mail')
        member.date_of_birth = request.POST.get('date-of-birth')
        member.place_of_birth = request.POST.get('place-of-birth')
        member.city_of_residence = request.POST.get('city-of-residence')
        member.phone_number = request.POST.get('phone-number')

        member.user.save()
        member.save()

        messages.success(request, "Le membre a été mis à jour avec succès.")
        return redirect('update_member')

    members_list = Member.objects.all()
    context = {
        'name': 'update_member',
        'members_list': members_list
    }
    return render(request, 'librarians/update_member.html', context)
