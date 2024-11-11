import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from librarians.models_members import Member


@pytest.fixture
def multiple_members(db):
    user1 = User.objects.create(
        username="Pierre Dupont",
        first_name="Pierre",
        last_name="Dupont",
        email="pierre.dupont@example.com"
    )
    member1 = Member.objects.create(
        user=user1,
        date_of_birth="2000-01-01",
        place_of_birth="Paris",
        city_of_residence="Paris",
        phone_number="0606060606",
        borrowings_number=0
    )

    user2 = User.objects.create(
        username="Paul Dupuis",
        first_name="Paul",
        last_name="Dupuis",
        email="paul.dupuis@example.com"
    )
    member2 = Member.objects.create(
        user=user2,
        date_of_birth="2000-01-01",
        place_of_birth="Marseille",
        city_of_residence="Marseille",
        phone_number="0606060607",
        borrowings_number=0
    )

    user3 = User.objects.create(
        username="Jacques Dubois",
        first_name="Jacques",
        last_name="Dubois",
        email="jacques.dubois@example.com"
    )
    member3 = Member.objects.create(
        user=user3,
        date_of_birth="2000-01-01",
        place_of_birth="Lyon",
        city_of_residence="Lyon",
        phone_number="0606060608",
        borrowings_number=0
    )

    return [member1, member2, member3]

@pytest.mark.django_db
def test_display_members(client, multiple_members):
    # Simule une requête GET client pour accéder à l'URL de la page display_members
    response = client.get(reverse('display_members'))

    # Vérifie si l'opération est un succès
    assert response.status_code == 200

    # Vérifie la présence des membres issus de la BDD en vérifiant la présence de leur prénom sur l'interface utilisateur
    assert "Pierre" in response.content.decode()
    assert "Paul" in response.content.decode()
    assert "Jacques" in response.content.decode()