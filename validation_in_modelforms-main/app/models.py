from django.db import models

# Create your models here.
from django.core import validators

class Student(models.Model):
    stname=models.CharField(max_length=100,validators=[validators.MinLengthValidator(5)])
    stage=models.IntegerField()
    stemail=models.EmailField()
    stmobile=models.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
