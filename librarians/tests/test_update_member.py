import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from librarians.models_members import Member
from django.contrib.messages import get_messages
from datetime import date


@pytest.fixture
def new_member(db):
    # Création d'un membre en BDD
    user = User.objects.create(
        username="Pierre Dupont",
        first_name="Pierre",
        last_name="Dupont",
        email="pierre.dupont@example.com"
    )
    member = Member.objects.create(
        user=user,
        date_of_birth="2000-01-01",
        place_of_birth="Paris",
        city_of_residence="Paris",
        phone_number="0606060606",
        borrowings_number=0
    )
    return member


@pytest.mark.django_db
def test_update_member(client, new_member):
    # Données mises à jour du membre initial
    update_data = {
        'member-id': new_member.id,
        'first-name': 'Paul',
        'last-name': 'Dupuis',
        'e-mail': 'paul.dupuis@example.com',
        'date-of-birth': '2002-02-02',
        'place-of-birth': 'Marseille',
        'city-of-residence': 'Nice',
        'phone-number': '0606060607',
    }

    # Envoi de la requête POST pour mettre à jour le membre
    response = client.post(reverse('update_member'), update_data, follow=True)

    # Vérifie que la redirection et le message sont présents
    assert response.status_code == 200
    messages = list(get_messages(response.wsgi_request))
    assert any("Le membre a été mis à jour avec succès." in message.message for message in messages)

    # Récupération du membre depuis la BDD et vérification de la mise à jour de ces données
    new_member.refresh_from_db()
    assert new_member.user.first_name == "Paul"
    assert new_member.user.last_name == "Dupuis"
    assert new_member.user.email == "paul.dupuis@example.com"
    assert new_member.date_of_birth == date(2002, 2, 2)
    assert new_member.place_of_birth == "Marseille"
    assert new_member.city_of_residence == "Nice"
    assert new_member.phone_number == "0606060607"