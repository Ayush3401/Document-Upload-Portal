from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *

# Create your views here.


def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        user=User.objects.get(username=request.POST.get('username'))
        user.is_staff=True
        user.save()
        folder = Folder.objects.create(name = 'Home')
        folder.save()
        ufr = User_folder_relation.objects.create(user = user)
        ufr.folders.add(folder)
        ufr.save()
        return redirect('login')
    return render(request, 'main/signup.html', {'form': form})


@login_required(login_url='login')
def uploadFile(request, folder_id):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            file = File.objects.create(
                name=request.POST['name'], file=request.FILES['file'])
            Folder.objects.get(pk=folder_id).files.add(file)
            link = '/'+str(folder_id)+'/files/'
            return redirect(link)
    else:
        form = UploadFileForm()
    return render(request, 'main/upload.html', {'form': form})


@login_required(login_url='login')
def folder_view(request):
    user_folder_rel = User_folder_relation.objects.get(user = request.user)
    folders = user_folder_rel.folders.all()
    if request.method == 'POST':
        if 'delete' in request.POST:
            for folder in folders:
                if(str(folder.id) in request.POST):
                    user_folder_rel.folders.remove(folder)
                    print('here')
                    folder.delete()
            return redirect('home')
        if 'share' in request.POST:
            for folder in folders:
                if(str(folder.id) in request.POST):
                    user = User.objects.get(
                        username=request.POST.get('sharename'))
                    if user :
                        
                        ufr = User_folder_relation.objects.get(user=user)
                        if folder in ufr.folders.all() :
                            return HttpResponse('folder already exist')
                        else :
                            ufr.folders.add(folder)
                    else:
                        return HttpResponse('User does not exist')
    return render(request, 'main/folder_view.html', {'folders' : folders})


@login_required(login_url='login')
def file_view(request, folder_id):
    
    folder = Folder.objects.get(pk=folder_id)
    files = folder.files.all()

    if request.method == 'POST':
        if 'delete' in request.POST:
            for file in files:
                if(str(file.id) in request.POST):
                    folder.files.remove(file)
                    file.delete()
            return redirect('view_files', folder_id=folder_id)
        if 'share' in request.POST:
            for file in files:
                if(str(file.id) in request.POST):
                    try:
                        user = User.objects.get(username = request.POST.get('sharename'))
                        ufr = User_folder_relation.objects.get(user = user)
                        folder_name = 'Shared-' + str(request.user.username)
                        try:                            
                            folder = ufr.folders.get(name = folder_name)
                            folder.files.add(file)
                        except:
                            folder = Folder.objects.create(name=folder_name)
                            ufr.folders.add(folder)
                            folder.files.add(file)
                    except:
                        return HttpResponse('User does not exist')
        link = '/'+str(folder_id)+'/files/'
        return redirect(link)
    
    return render(request, 'main/fileview.html', {'files': files, 'folder': folder})


@login_required(login_url='login')
def create_folder(request):
    form = folderCreationForm()
    if request.method == 'POST':
        folder = Folder.objects.create(name = request.POST.get('name'))
        ufr = User_folder_relation.objects.get(user = request.user)
        ufr.folders.add(folder)
        return redirect('/home/')
    return render(request, 'main/createfolder.html', {'form' : form})

