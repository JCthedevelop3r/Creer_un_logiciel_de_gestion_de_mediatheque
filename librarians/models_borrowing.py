from django.db import models
from .models_members import Member
from .models_medias import Media


class Borrowing(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    borrowing_date = models.DateField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.member.user.first_name} {self.member.user.last_name} {self.media.name} {self.media.type}"
