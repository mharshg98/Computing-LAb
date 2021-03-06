from django.shortcuts import render,redirect
from django.http import JsonResponse
#from rest_framework.response import Response
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
from django.http import HttpResponse
from .models import Announcement,Enroll_Data,RegisteredStudents,FrontImage

def index(request):
    data_img=FrontImage.objects.all()
    data_ann=Announcement.objects.all()
    return render(request,'admin1/index.html',{'img':data_img,'annoc':data_ann})

def campus(request):
    return render(request,'admin1/campus.html')

def history(request):
    return render(request, 'admin1/history.html')

def programs(request):
    return render(request, 'admin1/programs.html')
def ranking(request):
    return render(request, 'admin1/ranking.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def adminLogin(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['Password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            if user.is_superuser:
                auth.login(request, user)
                return redirect('addnotice')
            else:
                auth.logout(request)
                messages.info(request,"Invalid Credentials !!")
                return redirect('/adminLogin')
        else:
            messages.info(request,"Invalid Credentials !!")
            return redirect('/adminLogin')
    else:
        return render(request,'admin1/adminLogin.html')

def addnotice(request):
    if request.method== 'GET':
        return render(request,'admin1/add_notice.html',{'flag_done':False})
    else:
        title = request.POST['title']
        subtitle = request.POST['subtitle']
        desc=request.POST['desc']
        file = request.FILES.get('file')
        data = Announcement.objects.create(file=file,title=title,subtitle=subtitle,desc=desc)
        return render(request,'admin1/add_notice.html',{'flag_done':True})

def shownotice(request):
    if request.method=='GET':
        data=Announcement.objects.all().order_by('-time')
        return render(request,'admin1/show_notice.html',{'data':data})
import json
def deletenotice(request):
    if request.method == "POST":
        id=request.POST["id"]
        Announcement.objects.filter(id=id).delete()
        response={'done':True}
        print("deleted")
        return HttpResponse(json.dumps(response))

def addStudent(request):
    if(request.method=='GET'):
        return render(request,'admin1/addstudent.html')
    else:
        file = request.FILES.get('enroll_list')
        enroll_Data = Enroll_Data.objects.create(enroll_datasheet = file)
        enroll_datasheet_path = enroll_Data.enroll_datasheet.path
        import csv
        rows = []
        with open(enroll_datasheet_path, 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                rows.append(row)
        print(header)
        for i in rows:
            Data = RegisteredStudents.objects.create(Reg_no=i[0],roll_no=i[1],branch=i[2],course=i[3],name=i[4],session=i[5],email=i[6],mobile=i[7])
        return render(request,'admin1/addstudent.html',{'message':'Data Saved Successfully'})

def showstudent(request):
    if request.method=='GET':
        data=RegisteredStudents.objects.all()
        return render(request,'admin1/showstudent.html',{'data':data})

def uploadhomeimage(request):
    if request.method == "GET":
        data = FrontImage.objects.all()
        return render(request, 'admin1/uploadhomeimage.html',{'data':data,'flag_done':False})
    else:
        title = request.POST['title']
        file = request.FILES.get('file')
        data = FrontImage.objects.create(image=file,title=title)
        data = FrontImage.objects.all()
        return render(request,'admin1/uploadhomeimage.html',{'data':data,'flag_done':True})

def deleteImageData(request):
    if request.method == "POST":
        id=request.POST["id"]
        FrontImage.objects.filter(id=id).delete()
        response={'done':True}
        print("deleted")
        return HttpResponse(json.dumps(response))
