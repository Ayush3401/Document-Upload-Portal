from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    roll_number = models.IntegerField(default=0)
    REQUIRED_FIELDS = ['roll_numer']
