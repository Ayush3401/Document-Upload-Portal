from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class usercreationform(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

        
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file']


class folderCreationForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']
    