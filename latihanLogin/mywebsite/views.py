from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def homeView(request):
    return render(request,'home.html')

def profil(request):
    #user permission check
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'profil.html')

def loginView(request):
    form = LoginForm(request.POST or None)

    if request.method == 'GET':
        if request.user.is_authenticated():
            return redirect('profil')
        else:
            return render(request, 'login.html', {'form':form})
    
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('profil')    
        else:
            return redirect('login')

@login_required(login_url='login') # agar user yang tidak login tidak bisa mengakses logout
def logoutView(request):
    logout(request)
    return redirect('login')

def signupView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            new_user = authenticate(request,username=username,password=password)
            login(request,new_user)
            return redirect('profil')
    else:
        form = RegisterForm()
    
    return render(request, 'signup.html', {'form':form})