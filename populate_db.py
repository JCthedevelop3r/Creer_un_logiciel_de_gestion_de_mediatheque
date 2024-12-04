from librarians.models_medias import Book, Cd, Board_game, Dvd
from librarians.models_members import Member
from librarians.models_borrowing import Borrowing
from django.contrib.auth.models import User
from datetime import date, timedelta
from django.contrib.contenttypes.models import ContentType
from django.db import transaction


def populate():
    try:
        # Démarre une transaction
        with transaction.atomic():
            # Données des médias
            books = [
                {'name': 'Le Seigneur des anneaux', 'author': 'J. R. R. Tolkien', 'type': 'book', 'quantity': 2},
                {'name': 'Harry Potter', 'author': 'J. K. Rowling', 'type': 'book', 'quantity': 2},
            ]

            cds = [
                {'name': 'Baby', 'artist': 'Justin Bieber', 'type': 'cd', 'quantity': 2},
                {'name': 'Thriller', 'artist': 'Michael Jackson', 'type': 'cd', 'quantity': 2},
            ]

            board_games = [
                {'name': 'Monopoly', 'creator': 'Hasbro', 'type': 'board_game', 'quantity': 10},
                {'name': 'Unlock', 'creator': 'Space Cowboys', 'type': 'board_game', 'quantity': 3},
            ]

            dvds = [
                {'name': 'Le Roi lion', 'director': 'Roger Allers, Rob Minkoff', 'type': 'dvd', 'quantity': 3},
                {'name': 'Inception', 'director': 'Christopher Nolan', 'type': 'dvd', 'quantity': 4},
            ]

            # Création des médias
            for book in books:
                Book.objects.create(
                    name=book['name'],
                    author=book['author'],
                    type=book['type'],
                    quantity=book['quantity']
                )

            for cd in cds:
                Cd.objects.create(
                    name=cd['name'],
                    artist=cd['artist'],
                    type=cd['type'],
                    quantity=cd['quantity']
                )

            for board_game in board_games:
                Board_game.objects.create(
                    name=board_game['name'],
                    creator=board_game['creator'],
                    type=board_game['type'],
                    quantity=board_game['quantity']
                )

            for dvd in dvds:
                Dvd.objects.create(
                    name=dvd['name'],
                    director=dvd['director'],
                    type=dvd['type'],
                    quantity=dvd['quantity']
                )

            print("Les médias ont été créés avec succès.")

            # Données des membres
            users = [
                {'first-name': 'John', 'last-name': 'Doe', 'email': 'john.doe@example.com'},
                {'first-name': 'Jane', 'last-name': 'Doe', 'email': 'jane.doe@example.com'},
                {'first-name': 'Paul', 'last-name': 'Dupont', 'email': 'paul.dupont@example.com'}
            ]

            members = [
                {'user': users[0], 'date-of-birth': '1995-05-25', 'place-of-birth': 'New-York',
                 'city-of-residence': 'Miami',
                 'phone-number': '0606060606', 'borrowings-number': 3},
                {'user': users[1], 'date-of-birth': '2000-07-27', 'place-of-birth': 'Los Angeles',
                 'city-of-residence': 'Miami',
                 'phone-number': '0606060607', 'borrowings-number': 1},
                {'user': users[2], 'date-of-birth': '2005-09-29', 'place-of-birth': 'Lille',
                 'city-of-residence': 'Paris',
                 'phone-number': '0606060608', 'borrowings-number': 0}
            ]

            # Création des membres
            created_users = []
            for user in users:
                created_user = User.objects.create(
                    first_name=user['first-name'],
                    last_name=user['last-name'],
                    email=user['email'],
                    username=f"{user['first-name']}.{user['last-name']}".lower()
                )
                created_users.append(created_user)

            for i, member in enumerate(members):
                Member.objects.create(
                    user=created_users[i],
                    date_of_birth=member['date-of-birth'],
                    place_of_birth=member['place-of-birth'],
                    city_of_residence=member['city-of-residence'],
                    phone_number=member['phone-number'],
                    borrowings_number=member['borrowings-number']
                )

            print("Les membres ont été créés avec succès.")

            # Récupération des membres John et Jane Doe
            john = Member.objects.get(user__first_name='John', user__last_name='Doe')
            jane = Member.objects.get(user__first_name='Jane', user__last_name='Doe')

            # Récupération des médias pour John
            medias_john = [
                {'media': Book.objects.get(name="Le Seigneur des anneaux"), 'quantity': 1},
                {'media': Book.objects.get(name="Harry Potter"), 'quantity': 1},
                {'media': Cd.objects.get(name="Baby"), 'quantity': 1},
            ]

            # Création des emprunts de John
            for item in medias_john:
                media = item['media']
                content_type = ContentType.objects.get_for_model(media)
                Borrowing.objects.create(
                    member=john,
                    content_type=content_type,
                    object_id=media.id,
                    borrowing_date=date.today(),
                    due_date=date.today() + timedelta(days=7)
                )

            # Récupération du média pour Jane
            media_jane = [
                {'media': Cd.objects.get(name="Thriller"), 'quantity': 1}
            ]

            # Création de l'emprunt de Jane
            for item in media_jane:
                media = item['media']
                content_type = ContentType.objects.get_for_model(media)
                Borrowing.objects.create(
                    member=jane,
                    content_type=content_type,
                    object_id=media.id,
                    borrowing_date=date(2024, 11, 15),
                    due_date=date(2024, 11, 23)
                )

            print("Les emprunts ont été créés avec succès.")

            print("Base de données peuplée avec succès!")

    except Exception as e:
        print(f"Erreur pendant le peuplement de la base de données : {e}")
