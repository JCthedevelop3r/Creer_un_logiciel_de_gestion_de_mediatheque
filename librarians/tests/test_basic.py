import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_database_access():
    # Test basique pour vérifier l'accès à la base de données
    assert User.objects.count() == 0