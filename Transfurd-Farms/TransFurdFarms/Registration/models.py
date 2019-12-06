from django.db import models
from django.conf import settings
import datetime

# Create your models here.


class Animals(models.Model):
    animalType = models.CharField
    numberOfAnimals = models.IntegerField
    age = models.IntegerField
    vaccinationDate = models.DateTimeField
    maturityAge = models.DateTimeField


def __str__(self):
    return self.id
