from django.db import models

# Create your models here.
class School(models.Model):
    schoolname=models.CharField(max_length=100)
    slocation=models.CharField(max_length=100)
class student(models.Model):
    schoolname=models.ForeignKey('School',on_delete=models.CASCADE)
    sname=models.CharField(max_length=100)
