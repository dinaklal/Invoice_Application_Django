from django.db import models

# Create your models here.
class Sites(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=100)
    Unit_price = models.CharField(max_length=100)
