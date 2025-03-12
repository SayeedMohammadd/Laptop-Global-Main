from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png',upload_to='profile_pics')
    address = models.TextField(blank=True,max_length=100)
    full_name = models.TextField(blank=True,max_length=100)
    tel = models.TextField(blank=True,max_length=100)
    country = models.TextField(blank=True,max_length=100)
    city = models.TextField(blank=True,max_length=100)
    you_are = models.TextField(blank=True,max_length=100)

    def __str__(self):
        return f'{self.user.username} Profile'
