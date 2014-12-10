from django.db import models


# Create your models here.
class Address(models.Model):
    zip = models.IntegerField()
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=250)
    district = models.CharField(max_length=500)
    street = models.CharField(max_length=500)
    building = models.CharField(max_length=50)


class Dossier(models.Model):
    address = models.OneToOneField(Address)  # one address for one dossier