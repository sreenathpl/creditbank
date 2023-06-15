from django.contrib.auth.models import UserManager
from django.db import models

class user(models.Model):
    objects = UserManager()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

def __str__(self):
    return self.username

# Create your models here.
