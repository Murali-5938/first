from django.db import models

# Create your models here.
class Country(models.Model):
    country_name=models.CharField(max_length=100)


class Captial(models.Model):
    country_name=models.ForeignKey(Country,on_delete=models.CASCADE)
    captial_name=models.CharField(max_length=100)