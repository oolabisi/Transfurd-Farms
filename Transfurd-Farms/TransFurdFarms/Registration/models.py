from django.db import models
from django.conf import settings
import datetime

# Create your models here.


class Animals(models.Model):
    Number_Of_Animal = models.IntegerField
    Age = models.IntegerField
    Vaccination_Date = models.DateTimeField
    Marturity_Age = models.DateTimeField


def __str__(self):
    return self.id
