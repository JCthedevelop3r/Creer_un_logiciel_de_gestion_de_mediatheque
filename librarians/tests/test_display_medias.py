import pytest
from django.urls import reverse
from librarians.models_medias import Media, Book, Cd, Board_game, Dvd


@pytest.fixture
def multiple_medias():
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