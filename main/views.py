from django.shortcuts import render
from .forms import *

# Create your views here.
def signup(request):
    form = User_Create_form(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'main/signup.html', {'form' : form})
