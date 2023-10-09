from django.shortcuts import render
from django.contrib.auth.models import User
from accounts.models import User

def index(request):
    return render(request, 'index.html')

def adminreg(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        admin = User(username=username, email=email, phone=phone, password=password, type='admin')
        admin.is_superuser = True
        admin.is_staff = True
        admin.is_active = True
        admin.save()
    return render(request, 'adminreg.html')

def adminlogin(request):
    # if request.method == 'POST':
    #     username=request.POST.get('username')     
    #     password=request.POST.get('password')
    #     admin = authenticate(username=username, password=password)  
    return render(request, 'adminlogin.html')
        



def adminlogin(request):
    return render(request, 'adminlogin.html')