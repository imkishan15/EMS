import re
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from pro import settings
from django.http import HttpResponse, HttpRequest
from . models import Employee,Role,Department
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ap.models import Employee
from . serializers import TaskSerializer
from ap import serializers
from ap.models import Employee
from datetime import datetime
from django.db.models import Q

# Create your views here.

def home(request):
    return render(request, "home.html")

def signin(request):
    if request.method=="POST":
        username=request.POST['user']
        ps=request.POST['ps']

        user=authenticate(username=username, password=ps)

        if user is not None:
            login(request, user)
            fname=user.first_name
            return render(request, "index.html", {'fname': fname})

        else:
            return render(request, "wrong.html")


    return render(request, "signin.html")
    
def signup(request):
    if request.method=="POST":
        username=request.POST['user']
        fn=request.POST['fn']
        ln=request.POST['ln']
        email=request.POST['email']
        ps1=request.POST['ps1']
        ps2=request.POST['ps2']

   
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('signup')
        
        if ps1 != ps2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signup')



        myuser=User.objects.create_user(username,email,ps1)
        myuser.first_name=fn
        myuser.last_name=ln
        myuser.email=email

        myuser.save()
        messages.success(request, "Your account is successsfully created!!!, check your email!!!")

        return render(request, "signups.html")


    return render(request, "signup.html")

def signout(request):
    logout(request)
    return redirect('home')

def index(request):
    return render(request, "index.html")

def hom(request):
    return render(request, "index.html")

def view(request):
    emps=Employee.objects.all()
    context={
        'emps': emps
    }
    print(context)
    return render(request, "view.html", context)

def add(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept=request.POST['dept']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        role=request.POST['role']

        new_emp=Employee(first_name=first_name,last_name=last_name,dept=dept,salary=salary,bonus=bonus,phone=phone,role=role,date=datetime.now())
        new_emp.save()
        return render(request, "ads.html")

    return render(request, "add.html")

def remove(request, emp_id=0):
    if emp_id:
        emp_remove=Employee.objects.get(id=emp_id)
        emp_remove.delete()
        return render(request, "rs.html")
    emps=Employee.objects.all()
    contex={
        'emps': emps
    }
    print(contex)
    return render(request, "remove.html", contex)

def filter(request):
    if request.method=="POST":
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emp=Employee.objects.all()
        if name:
            emps=emp.filter(Q(first_name__icontains=name)|Q(last_name__icontains=name))
        if dept:
            emps=emp.filter(dept=dept)
        if role:
            emps=emp.filter(role=role)

        conten={
        'emps': emps
        }
        return render(request, "view.html", conten)

    return render(request, "filter.html")

@api_view(['GET'])
def apiview(request):
    api_urls={
        'List':'/emp-list/',
        'Detail View':'/emp-detail</str:pk>/',
        'Create':'/emp-create/',
        'Update':'/emp-update</str:pk>/',
        'Delete':'/emp-delete</str:pk>/',
    }
    return Response(api_urls)
@api_view(['GET'])
def empList(request):
    tasks=Employee.objects.all()
    serializer=TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def empDetail(request,pk):
    tasks=Employee.objects.get(id=pk)
    serializer=TaskSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def empCreate(request):
    serializer=TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def empUpdate(request,pk):
    tasks=Employee.objects.get(id=pk)
    serializer=TaskSerializer(instance=tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def empDelete(request,pk):
    tasks=Employee.objects.get(id=pk)
    tasks.delete()
    return Response("Itam deleted successfully")