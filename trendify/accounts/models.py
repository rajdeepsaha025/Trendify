from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(unique=True, max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)
    # pfp = models.ImageField(upload_to='static\img\pfp', 6blank=True, null=True)
    # password = models.CharField(max_length=20)
    location = models.CharField(max_length=30)
    type = models.CharField(max_length=20, choices=[("admin", "Admin"), ("editor", "Editor"), ("user", "User")])

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email' , 'phone' , 'password']

    def __str__(self):
        return self.username