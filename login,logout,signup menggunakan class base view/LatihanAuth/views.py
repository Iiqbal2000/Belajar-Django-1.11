from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm,LoginForm
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy


def index(request):

    context = {
        'page_title':'Home',
    }

    return render(request, 'index.html', context)

def profil(request):
    
    #user permission check
    if not request.user.is_authenticated:
        return redirect('login')

    nameUser = request.user.get_username()

    context = {
        'page_title':'Selamat Datang',
        'name':nameUser
    }

    return render(request, 'profil.html', context)

# menggunakan CBV
class RegisterViewCbv(CreateView):
    template_name = 'signup.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

class LoginViewCbv(LoginView):
    template_name = 'login.html'
    
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated():
            return redirect('profil')
        
        return super().get(*args,**kwargs)

class LogoutViewCbv(LogoutView):
    pass
