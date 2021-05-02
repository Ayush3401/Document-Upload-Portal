from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')

class Folder(models.Model):
    name = models.CharField(max_length=255)
    files = models.ManyToManyField(File)

class User_folder_relation(models.Model):
    folders = models.ManyToManyField(Folder)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Folder_folder_relation(models.Model):
    parent = models.ForeignKey(
        Folder, on_delete=models.CASCADE, related_name='parent_folder')
    children = models.ManyToManyField(Folder)
