from django.db import models
from django.contrib.auth.models import User

class Vendorshop(models.Model):
    Owner=models.ForeignKey(User, on_delete=models.CASCADE)
    Shopname=models.CharField(max_length=100)
    Businesstype=models.CharField(max_length=100)
    Latitude=models.FloatField()
    Longitude=models.FloatField()

    def __str__(self):
        return self.Shopname


# Create your models here.
