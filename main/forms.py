from django import forms
from .models import *
from django.contrib.auth.models import User


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file']


class folderCreationForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']
