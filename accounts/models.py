from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    nickname=models.CharField(max_length=10, null=True, blank=True)
    report=models.IntegerField(null=True, blank=True)
    
    profile_choices=[
        ("cd","cd"),
        ("mic","mic"),
        ("headset","headset")
    ]
    profile=models.CharField(max_length=7, choices=profile_choices, null=True, blank=True)

    def __str__(self):
        return self.username

    #confirm_password=models.CharField(max_length=128, default='')
