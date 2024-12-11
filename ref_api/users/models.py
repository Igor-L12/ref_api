from django.contrib.auth.models import AbstractUser
from django.db import models


class UserPhone(AbstractUser):
    phone_number = models.CharField(max_length=12, blank=False, unique=True) 
    invite_code = models.CharField(max_length=6, blank=False, unique=True)