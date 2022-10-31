from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from accounts.forms import MyUserCreationForm,EditProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
from accounts.models import UserExtension
# Create your views here.
def mi_login(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario) #django_login(request, usuario)
            extension_user,is_new = UserExtension.objects.get_or_create(user=request.user)
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

@login_required
def profile(request):
    extension_user,is_new = UserExtension.objects.get_or_create(user=request.user)
    
    return render(request,'accounts/profile.html',{})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        formulario = EditProfileForm(request.POST, request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data
            request.user.first_name = data['first_name']
            request.user.last_name = data['last_name']
            request.user.email = data['email']
            request.user.userextension.avatar = data['avatar']
            request.user.userextension.page = data['page']
            request.user.userextension.description = data['description']
            request.user.userextension.phone_number = data['phone_number']
            request.user.userextension.job = data['job']
            request.user.userextension.address = data['address']
            
            
            request.user.userextension.save()
            request.user.save()
            return redirect('profile')
    else:
        formulario = EditProfileForm(
            initial={
                    'first_name':request.user.first_name,
                    'last_name':request.user.last_name,
                    'email':request.user.email,
                    'avatar':request.user.userextension.avatar,
                    'page':request.user.userextension.page,
                    'description':request.user.userextension.description,
                    'phone_number':request.user.userextension.phone_number,
                    'job':request.user.userextension.job,
                    'address':request.user.userextension.address,
                    })
    return render(request,'accounts/edit_profile.html',{'formulario':formulario})

class ChangePassword(LoginRequiredMixin,PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = '/accounts/profile'