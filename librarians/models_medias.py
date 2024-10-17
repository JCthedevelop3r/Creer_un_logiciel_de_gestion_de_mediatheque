from django.db import models


# Create your models here.
class Media(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=15, default='Default Type')
    borrowing_date = models.DateField()
    available = models.BooleanField(default=True)
    borrowers_number = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
