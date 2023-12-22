from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    
    return render(request, 'home.html')


##############################################
def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        passwd1 = request.POST['password1']
        passwd2 = request.POST['password2']
        
        if passwd1 == passwd2:
            myuser = User.objects.create_user(uname, email, passwd1)
            myuser.save()
        else:
            return HttpResponse("Your Password does not match ")
        
        return redirect('login')
    
    return render(request, 'signup.html')


#########################################
def LoginPage(request):
    if request.method=="POST":
        uname = request.POST['username']
        passwd = request.POST['password']
        user = authenticate(request, username=uname, password=passwd)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Incorrect Username or Password")
    
    return render(request, 'login.html')


@login_required(login_url='login')
def LogoutPage(request):
    logout(request)
    return redirect('login')