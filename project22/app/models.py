from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=1000)
    published_date=models.DateField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    author_name=models.CharField(max_length=100)
    content=models.CharField(max_length=1000)
    created_date=models.DateField()
    def __str__(self):
        return self.author_name