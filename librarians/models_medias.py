from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    borrowing_date = models.DateField(null=True, blank=True)
    available = models.BooleanField(default=True)
    borrowers_number = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.author}"


class Cd(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    borrowing_date = models.DateField(null=True, blank=True)
    available = models.BooleanField(default=True)
    borrowers_number = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.artist}"


class Board_game(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.creator}"


class Dvd(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    borrowing_date = models.DateField(null=True, blank=True)
    available = models.BooleanField(default=True)
    borrowers_number = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.director}"
