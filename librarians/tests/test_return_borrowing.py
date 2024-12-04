import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from librarians.models_borrowing import Borrowing
from librarians.models_medias import Book
from librarians.models_members import Member
from django.utils import timezone
from datetime import timedelta
from django.contrib.contenttypes.models import ContentType


@pytest.mark.django_db
def test_return_borrowing(client):
    # Création des objets nécessaires
    user = User.objects.create(
        username="john_doe",
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com"
    )
    member = Member.objects.create(
        user=user,
        date_of_birth="2000-01-01",
        place_of_birth="Paris",
        city_of_residence="Marseille",
        phone_number="0123456789",
        borrowings_number=1
    )
    book = Book.objects.create(
        name='Le Seigneur des anneaux',
        type='book',
        author='J. R. R. Tolkien',
        quantity=2
    )
    borrowing = Borrowing.objects.create(
        member=member,
        content_type=ContentType.objects.get_for_model(book),
        object_id=book.id,
        due_date=timezone.now().date() + timedelta(days=7)
    )

    # Simulation de la requête POST pour retourner l'emprunt
    data = {
        'borrowing_ids': [borrowing.id],
        f'member_id_{borrowing.id}': member.id,
    }
    response = client.post(reverse('return_borrowing'), data, follow=True)

    assert response.status_code == 200

    messages = list(get_messages(response.wsgi_request))
    assert any("Les emprunts ont été rentrés avec succès." in message.message for message in messages)

    # Vérification de la suppression de l'emprunt
    assert Borrowing.objects.count() == 0

    # Vérification des mises à jour du média et du membre
    book.refresh_from_db()
    member.refresh_from_db()
    assert book.quantity == 3  # Augmenté après le retour
    assert member.borrowings_number == 0  # Réduit après le retour
