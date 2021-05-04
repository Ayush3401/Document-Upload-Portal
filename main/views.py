from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import JsonResponse
from .forms import *
from .models import *

# Create your views here.


def firstpage(request):
    return render(request, "main/firstpage.html")


def signup(request):
    form = usercreationform(request.POST or None)
    if form.is_valid():
        form.save()
        user = User.objects.get(username=request.POST.get('username'))
        user.is_staff = True
        user.save()
        folder = Folder.objects.create(name='Home')
        folder.save()
        ufr = User_folder_relation.objects.create(user=user)
        Folder_folder_relation.objects.create(parent=folder)
        ufr.folders.add(folder)
        ufr.save()
        return redirect('login')
    return render(request, 'main/signup.html', {'form': form})


@login_required(login_url='login')
def uploadFile(request, folder_id):
    if request.method == 'POST':
        print(request.FILES)
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():

            file = File.objects.create(
                name=request.FILES['file'].name, file=request.FILES['file'])
            Folder.objects.get(pk=folder_id).files.add(file)
            link = '/'+str(folder_id)+'/files/'
            return redirect(link)
    else:
        form = UploadFileForm()
    return render(request, 'main/upload.html', {'form': form})


@login_required(login_url='login')
def folder_view(request):
    user_folder_rel = User_folder_relation.objects.get(user=request.user)
    folders = user_folder_rel.folders.all()
    if request.method == 'POST':
        if 'delete' in request.POST:
            for folder in folders:
                if(str(folder.id) in request.POST):
                    user_folder_rel.folders.remove(folder)
            return redirect('home')
        if 'share' in request.POST:
            for folder in folders:
                if(str(folder.id) in request.POST):
                    user = User.objects.get(
                        username=request.POST.get('sharename'))
                    if user:

                        ufr = User_folder_relation.objects.get(user=user)
                        if folder in ufr.folders.all():
                            return HttpResponse('folder already exist')
                        else:
                            ufr.folders.add(folder)
                    else:
                        return HttpResponse('User does not exist')
    else:
        if 'term' in request.GET:
            names = []
            val = str(request.GET.get('term'))
            users = User.objects.filter(username__icontains=val)
            for term in users:
                names.append(term.username)
            return JsonResponse(names, safe=False)

    return render(request, 'main/folder_view.html', {'folders': folders})


@login_required(login_url='login')
def file_view(request, folder_id):

    folder = Folder.objects.get(pk=folder_id)
    files = folder.files.all()
    ffr = Folder_folder_relation.objects.get(parent=folder)
    folders = ffr.children.all()
    ufr = User_folder_relation.objects.get(user=request.user)

    if request.method == 'POST':
        if 'delete' in request.POST:
            print(request.POST)
            for file in files:
                id='file'+str(file.id)
                if(id in request.POST):
                    print("HERE")
                    folder.files.remove(file)
            for child_folder in folders:
                id='folder'+str(child_folder.id)              
                if(id in request.POST):
                    print("FOLDER")
                    ffr.children.remove(child_folder)
            return redirect('view_files', folder_id=folder_id)
        elif 'share' in request.POST:
            for file in files:
                id='file'+str(file.id)
                if(id in request.POST):
                        user = User.objects.get(
                            username=request.POST.get('sharename'))
                        ufr = User_folder_relation.objects.get(user=user)
                        folder_name = 'Shared-' + str(request.user.username)
                        try:
                            fldr = ufr.folders.get(name=folder_name)
                            fldr.files.add(file)
                        except:
                            fldr = Folder.objects.create(name=folder_name)
                            fldr.save()
                            ffffr=Folder_folder_relation.objects.create(parent=fldr)
                            ufr.folders.add(fldr)
                            fldr.files.add(file)
            
            for child_folder in folders:
                id="folder"+str(child_folder.id)
                if(id in request.POST):
                        user = User.objects.get(
                            username=request.POST.get('sharename'))
                        ufr = User_folder_relation.objects.get(user=user)
                        ufr.folders.add(child_folder)
                     

        elif 'move' in request.POST:
            for file in files:
                id='file'+str(file.id)
                if(id in request.POST):
                    fldr = ufr.folders.get(
                        pk=request.POST.get('movename'))
                    folder.files.remove(file)
                    fldr.files.add(file)

            for child_folder in folders:
                id='folder'+str(child_folder.id)
                if(id in request.POST):
                    fffr = Folder_folder_relation.objects.get(parent=Folder.objects.get(
                        pk=request.POST.get('movename')))
                    ffr.children.remove(child_folder)
                    fffr.children.add(child_folder)

        return redirect('view_files', folder_id)
    else:
        if 'term' in request.GET:
            names = []
            val = str(request.GET.get('term'))
            users = User.objects.filter(username__icontains=val)
            for term in users:
                names.append(term.username)
            return JsonResponse(names, safe=False)

    return render(request, 'main/fileview.html', {'files': files, 'folders': folders, 'folder': folder, 'pk': folder_id})


@login_required(login_url='login')
def create_folder(request, folder_id):
    form = folderCreationForm()
    if request.method == 'POST':
        folder = Folder.objects.create(name=request.POST.get('name'))
        print(request.POST)
        f = Folder_folder_relation.objects.create(parent=folder)
        folder.save()
        f.save()
        if(folder_id):
            ffr = Folder_folder_relation.objects.get(
                parent=Folder.objects.get(pk=folder_id))
            ffr.children.add(folder)
            link = '/' + str(folder_id) + '/files/'
            return redirect(link)
        else:
            ufr = User_folder_relation.objects.get(user=request.user)
            ufr.folders.add(folder)
            return redirect('/home/')
    return render(request, 'main/createfolder.html', {'form': form})


@login_required(login_url='login')
def renamefolder(request,parent_id, folder_id):
    folder = Folder.objects.get(pk=folder_id)
    if request.method == "POST":
        if 'newname' in request.POST:
            folder.name = request.POST.get('newname')
            folder.save()
            if(parent_id==0):
                return redirect('home')
            else:
                link ='/'+  str(parent_id) + '/files/'
                return redirect(link)
    return render(request, 'main/renamefolder.html')


@login_required(login_url='login')
def renamefile(request,parent_id, file_id):
    file = File.objects.get(pk=file_id)
    if request.method == "POST":
        if 'newname' in request.POST:
            file.name = request.POST.get('newname')
            file.save()
            if(parent_id == 0):
                return redirect('home')
            else:
                link ='/'+ str(parent_id) + '/files/'
                return redirect(link)
    return render(request, 'main/renamefile.html')
