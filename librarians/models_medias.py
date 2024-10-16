from django.db import models

# Create your models here.
class Media(models.Model):
    name = models.CharField(max_length=100)
    borrowing_date = models.DateField()
    available = models.BooleanField(default=True)
    borrower_member = models.CharField(max_length=50)
    borrower_number = models.IntegerField()
    quantity = models.IntegerField()

"""
l'attribut du créateur (author, director, artist...) devra être ajouté au moment de l'instanciation des objets.
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    borrowing_date = models.DateField()
    available = models.BooleanField(default=True)
    borrower = models.CharField(max_length=50)


class Dvd(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=50)
    borrowing_date = models.DateField()
    available = models.BooleanField(default=True)
    borrower = models.CharField(max_length=50)


class Cd(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    borrowing_date = models.DateField()
    available = models.BooleanField(default=True)
    borrower = models.CharField(max_length=50)


class BoardGame(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=50)
"""