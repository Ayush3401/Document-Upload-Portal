from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    roll_number = models.IntegerField(default=0)


class File(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User)
    file = models.FileField(upload_to='files/')
