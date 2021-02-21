from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import *
from .models import *

# Create your views here.


def signup(request):
    form = User_Create_form(request.POST or None)
    if form.is_valid():
        form.save()
        user=User.objects.all().get(username=request.POST.get('username'))
        user.is_staff=True
        user.save()
              
        return redirect('login')
    return render(request, 'main/signup.html', {'form': form})


@login_required(login_url='login')
def uploadFile(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            file = File.objects.create(
                name=request.POST['name'], file=request.FILES['file'])
            file.users.add(User.objects.get(pk=request.user.id))
            file.save()
            return redirect('signup')
    else:
        form = UploadFileForm()
    return render(request, 'main/upload.html', {'form': form})


def fileview(request):
    id = request.user.id
    files = File.objects.all().filter(pk=id)
    files = files.file
    return render(request,'main/fileview.html',{'files':files}) 
