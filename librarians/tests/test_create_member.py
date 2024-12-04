import pytest
from django.urls import reverse
from librarians.models_members import Member
from django.contrib.messages import get_messages


@pytest.mark.django_db
def test_create_member(client):
    # Données simulées pour le formulaire
    data = {
        'first-name': 'John',
        'last-name': 'Doe',
        'e-mail': 'john.doe@example.com',
        'date-of-birth': '2000-01-01',
        'place-of-birth': 'Paris',
        'city-of-residence': 'Paris',
        'phone-number': '0123456789',
    }

    # Envoi de la requête POST et suivi de la redirection (302) après le message de confirmation
    response = client.post(reverse('create_member'), data, follow=True)

    # Vérifie que la requête a bien été suivie jusqu'à un statut de succès
    assert response.status_code == 200

    # Vérifie la présence du message de succès dans le contexte
    messages = list(get_messages(response.wsgi_request))
    assert any(message.message == "Le membre a été créé avec succès." for message in messages)

    # Vérification de la création du membre en base de données
    assert Member.objects.count() == 1
    member = Member.objects.first()
    assert member.user.first_name == "John"
    assert member.user.last_name == "Doe"
    assert member.user.email == "john.doe@example.com"
