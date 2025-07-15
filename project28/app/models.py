from django.db import models

class Student(models.Model):
    sname=models.CharField(max_length=100)
    stage=models.IntegerField()
    smobile=models.CharField(max_length=10)
