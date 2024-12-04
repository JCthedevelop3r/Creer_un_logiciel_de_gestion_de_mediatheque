from django.db import models
from datetime import date, timedelta
from .models_members import Member
from .models_medias import Media


class Borrowing(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    borrowing_date = models.DateField(default=date.today)
    due_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.member.user.first_name} {self.member.user.last_name} {self.media.name} {self.media.type}"

    def save(self, *args, **kwargs):
        if self.due_date is None:  # Si la date d'échéance n'est pas définie
            self.due_date = date.today() + timedelta(days=7)  # Définir la date d'échéance ici
        super().save(*args, **kwargs)  # Appeler la méthode save parente
