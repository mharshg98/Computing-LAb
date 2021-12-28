
from django.shortcuts import render,redirect
from django.http import JsonResponse
#from rest_framework.response import Response
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
from django.http import HttpResponse
from Home.models import RegisteredStudents,Student

# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            if user.is_superuser == False:
                auth.login(request, user)
                return redirect('home')
            else:
                auth.logout(request)
                messages.info(request,"Invalid Credentials !!")
                return redirect('login')
        else:
            messages.info(request,"Invalid Credentials !!")
            print('hello')
            return redirect('login')
        
    else:
        return render(request,'student/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name=request.POST['name']
        email=request.POST['email']
        reg_no=request.POST['reg_no']
        roll_no=request.POST['roll_no']
        course=request.POST['course']
        branch=request.POST['branch']
        print(name,email,reg_no,roll_no,course,branch)
        if(RegisteredStudents.objects.filter(Reg_no=reg_no).exists()):
            data=RegisteredStudents.objects.filter(Reg_no=reg_no)
            x=data[0]
            if(x.name==name.strip() and x.email==email.strip() and x.Reg_no==reg_no.strip() and x.roll_no==roll_no.strip() and x.course==course.strip() and x.branch==branch.strip()):
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username taken please use other username')
                    return redirect('register')
                else:
                    user =User.objects.create_user(username=username,password=password,email=email,first_name=name,last_name=name)
                    user.save()
                    data1=Student.objects.create(id=user,branch=branch,course=course,Reg_no=reg_no,roll_no=roll_no,name=name,session=x.session,email=email,mobile=x.mobile,address=' ')
                    messages.info(request,"User created succesfully")
                    return redirect('login')
            else:
                messages.info(request,"Please Enter The Right Information")
                return redirect('register')
        else:
            messages.info(request,"Student does't exist")
            return redirect('register')

        
    else:
        return render(request,'student/register.html')

def home(request):
    user=request.user
    data=Student.objects.filter(id=user)
    rep=data[0]
    return render(request,"student/homepage.html",{'i':rep})

def editprofile(request):
    if(request.method=='POST'):
        email=request.POST['email']
        user=request.user
        phone=request.POST['mobile']
        add=request.POST['address']
        data=Student.objects.get(id=user)
        data.email=email
        data.mobile=phone
        data.address=add
        data.save()
        return redirect('home')
    return render(request, 'student/editprofile.html')