# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    

    phone_number = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
    
    def __str__(self):
        return self.username