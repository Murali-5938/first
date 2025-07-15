from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userregister(models.Models):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField()
    img=models.ImageField()