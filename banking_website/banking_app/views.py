from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import *


def home(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        un = request.POST['username']
        np = request.POST['password']
        cp = request.POST['Cpassword']
        if np == cp:
            if User.objects.filter(username=un).exists():
                messages.info(request, "!! Username already exists !!")
                return redirect('register')
            # elif User.objects.filter(email=el).exists():
            #     messages.info(request, "!! Email already exists !!")
            #     return redirect('register')
            else:
                user = User.objects.create_user(username=un, password=np)
                user.save()
                print("User Created")
                return redirect('login')

        else:
            messages.info(request, "!! Password mismatch !!")
            return redirect('register')
    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        un = request.POST['username']
        np = request.POST['password']
        user = auth.authenticate(username=un, password=np)
        if user is not None:
            auth.login(request, user)
            return render(request,'temp.html')
        else:
            messages.info(request, "Invalid details")
            return redirect('login')
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def temp(request):
    return render(request, 'temp.html')

def form(request):
    program = District.objects.all()
    d = {'program': program}
    return render(request,'form.html',d)

def load_courses(request):
    programming_id = request.GET.get('programming')
    courses = Branch.objects.filter(programming_id=programming_id).order_by('name')
    return render(request, 'branches.html', {'courses': courses})

def Approval(request):
    return render(request, 'Approval.html')

# Create your views here.
