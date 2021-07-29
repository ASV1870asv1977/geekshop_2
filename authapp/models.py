from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import datetime


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name = 'возраст')

    acttivation_key = models.CharField(max_lenght=128, blank=True)
    acttivation_key_