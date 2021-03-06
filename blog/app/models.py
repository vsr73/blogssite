from django.db import models
# Create your models here
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    dp = models.ImageField(null=True, default="avatar.svg")

''''
class Blogger(models.Model):
    host=models.ForeignKey(User,on_delete=models.CASCADE)
    dp=models.ImageField(null=True)


class Places(models.Model):
    name=models.CharField(max_length=500)'''

class Blogs(models.Model):
    blogger=models.ForeignKey(User,on_delete=models.CASCADE)
    topic=models.CharField(max_length=200,null=True)
    description= models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering= ['created']



class blogersupport(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=150)
    email=models.EmailField(max_length=200)
    message=models.TextField(null=True)

  


    