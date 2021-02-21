from django import forms
from django.contrib.auth.models import AbstractUser
from .models import *


class User_Create_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name',
                  'email', 'roll_number',  'password', ]
