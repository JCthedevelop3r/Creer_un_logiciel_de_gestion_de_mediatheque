import pytest
from django.urls import reverse
from librarians.models_medias import Media, Book
from django.contrib.messages import get_messages


@pytest.mark.django_db
def test_add_media(client):
    # Données simulées pour le formulaire
    data = {
        'media-name': 'Le Seigneur des anneaux',
        'media-type': 'book',
        'media-creator': 'J. R. R. Tolkien',
        'media-quantity': 2
    }

    response = client.post(reverse('add_media'), data, follow=True)

    assert response.status_code == 200

    messages = list(get_messages(response.wsgi_request))
    assert any(message.message == "Le média a été ajouté avec succès." for message in messages)

    assert Book.objects.count() == 1
    book = Book.objects.first()
    assert book.name == 'Le Seigneur des anneaux'
    assert book.author == 'J. R. R. Tolkien'
    assert book.type == 'book'
    assert book.quantity == 2

