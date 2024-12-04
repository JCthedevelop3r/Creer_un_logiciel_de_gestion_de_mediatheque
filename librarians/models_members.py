from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=50)
    city_of_residence = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    borrowings_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
