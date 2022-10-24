from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from accounts.forms import MyUserCreationForm

# Create your views here.
def mi_login(request):
   
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario) #django_login(request, usuario)
            return redirect('home')
    else:
        formulario = AuthenticationForm()
    return render(request,'accounts/login.html',{'formulario':formulario})

def register(request):
    if request.method == 'POST':
        formulario = MyUserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('home')
    else:
        formulario = MyUserCreationForm()
    return render(request,'accounts/register.html',{'formulario':formulario})