from django.shortcuts import render
from librarians.models_medias import Book, Cd, Board_game, Dvd


def home_members(request):
    books = Book.objects.all()
    cds = Cd.objects.all()
    board_games = Board_game.objects.all()
    dvds = Dvd.objects.all()

    context = {
        'books': books,
        'cds': cds,
        'board_games': board_games,
        'dvds': dvds,
    }
    return render(request, 'members/home_members.html', context)