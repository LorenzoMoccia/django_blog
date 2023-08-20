from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.CharField(max_length=400, default=0)
    author = models.CharField(max_length=30)
    likes = models.IntegerField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='img')