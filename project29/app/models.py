from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    sname=models.CharField(max_length=100)
    slocation=models.CharField
    def get_absolute_url(self):
        return reverse('Detail',kwargs={'pk':self.pk})



class Student(models.Model):
    sname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='School')
    stname=models.CharField(max_length=100)
    stage=models.IntegerField()
