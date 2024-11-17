import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from librarians.models_members import Member
from librarians.models_medias import Book
from librarians.models_borrowing import Borrowing


@pytest.mark.django_db
def test_create_borrowing(client):
    # Création d'un membre
    user = User.objects.create(username="john_doe", first_name="John", last_name="Doe", email="john.doe@example.com")
    member = Member.objects.create(
        user=user,
        date_of_birth="2000-01-01",
        place_of_birth="Paris",
        city_of_residence="Marseille",
        phone_number="0123456789",
        borrowings_number=0
    )

    # Création d'un média (par exemple un livre)
    book = Book.objects.create(name="Le Seigneur des anneaux", author="J.R.R. Tolkien", quantity=2)

    # Préparation des données du formulaire
    post_data = {
        'member_id': member.id,
        'media_ids': [book.id],  # Médias sélectionnés : le livre
    }

    # Envoi de la requête POST
    response = client.post(reverse('create_borrowing'), data=post_data, follow=True)

    # Vérification du statut de la réponse
    assert response.status_code == 200

    # Vérification que l'emprunt a été créé
    borrowings = Borrowing.objects.filter(member=member)
    assert borrowings.count() == 1  # Un emprunt a été créé

    # Vérification que l'emprunt est bien lié au livre sélectionné
    borrowing = borrowings.first()
    assert borrowing.content_type.model == 'book'  # Le type du contenu doit être 'book'
    assert borrowing.object_id == book.id  # L'objet emprunté doit être le livre créé

    # Vérification que la quantité du livre a bien été décrémentée
    book.refresh_from_db()
    assert book.quantity == 1  # La quantité du livre doit être de 1 après l'emprunt

    # Vérification que le nombre d'emprunts du membre a bien été mis à jour
    member.refresh_from_db()
    assert member.borrowings_number == 1  # Le nombre d'emprunts du membre doit être de 1

    # Vérification du message de succès
    messages = list(get_messages(response.wsgi_request))
    assert any("L'emprunt a été créé avec succès." in str(message) for message in messages)