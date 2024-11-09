from django.db import models


class Media(models.Model):
    name = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    quantity = models.IntegerField(null=True, blank=True)
    borrowing_date = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True  # Cette classe est abstraite, donc non instanciable directement

    def media_unavailable(self):
        if self.quantity is not None:
            self.available = self.quantity > 0

    def save(self, *args, **kwargs):
        self.media_unavailable()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Book(Media):
    author = models.CharField(max_length=100)
    type = models.CharField(max_length=15, default="book")

    def __str__(self):
        return f"{self.name} by {self.author}"


class Cd(Media):
    artist = models.CharField(max_length=100)
    type = models.CharField(max_length=15, default="cd")

    def __str__(self):
        return f"{self.name} by {self.artist}"


class Board_game(Media):
    creator = models.CharField(max_length=100)
    type = models.CharField(max_length=15, default="board_game")

    def __str__(self):
        return f"{self.name} by {self.creator}"


class Dvd(Media):
    director = models.CharField(max_length=100)
    type = models.CharField(max_length=15, default="dvd")

    def __str__(self):
        return f"{self.name} by {self.director}"
