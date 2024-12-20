import pytest
from django.urls import reverse
from librarians.models_medias import Book, Cd, Board_game, Dvd


@pytest.fixture
def multiple_medias(db):
    book = Book.objects.create(
        name='Le Seigneur des anneaux',
        author='J. R. R. Tolkien',
        type='book',
        quantity=int('2')
    )

    cd = Cd.objects.create(
        name='Baby',
        artist='Justin Bieber',
        type='cd',
        quantity=int('2')
    )

    board_game = Board_game.objects.create(
        name='Monopoly',
        creator='Hasbro',
        type='board_game',
        quantity=int('2')
    )

    dvd = Dvd.objects.create(
        name='Le Roi lion ',
        director='Roger Allers, Rob Minkoff',
        type='dvd',
        quantity=int('2')
    )

    return [book, cd, board_game, dvd]


@pytest.mark.django_db
def test_display_medias(client, multiple_medias):
    response = client.get(reverse('display_medias'))

    assert response.status_code == 200

    assert "Le Seigneur des anneaux" in response.content.decode()
    assert "book" in response.content.decode()
    assert "Baby" in response.content.decode()
    assert "cd" in response.content.decode()
    assert "Monopoly" in response.content.decode()
    assert "board_game" in response.content.decode()
    assert "Le Roi lion" in response.content.decode()
    assert "dvd" in response.content.decode()


@pytest.mark.django_db
def test_delete_media(client, multiple_medias):
    response = client.get(reverse('display_medias'))
    assert response.status_code == 200
    assert "Le Seigneur des anneaux" in response.content.decode()
    assert "book" in response.content.decode()

    # Préparation du média à supprimer : "Le Seigneur des anneaux"
    book = multiple_medias[0]
    delete_data = {
        'media-id': book.id,
        'media-type': book.type,
    }

    # Envoi d'une requête POST simulant le clic sur le bouton "Supprimer"
    response = client.post(reverse('display_medias'), delete_data, follow=True)
    assert response.status_code == 200

    # Vérification de l'abscence du média
    response = client.get(reverse('display_medias'))
    assert "Le Seigneur des anneaux" not in response.content.decode()
