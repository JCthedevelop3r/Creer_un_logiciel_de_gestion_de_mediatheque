import pytest
from django.urls import reverse
from librarians.models_medias import Media, Book, Cd, Board_game, Dvd


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