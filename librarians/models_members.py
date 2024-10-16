from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    name = models.CharField(User, max_length=50)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=50)
    city_of_residence = models.CharField(max_length=50)
    phone_number = models.Charfield(max_length=10)
    email = models.CharField(User, max_length=50)
    borrowing_member = models.ForeignKey(User, on_delete=models.CASCADE)
    # obstruct = models.BooleanField(default=False)