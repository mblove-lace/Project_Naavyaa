from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    # title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
        

