from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm):
    email = forms.CharField(label='Email', max_length = 20)
    password1: forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2: forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User 
        fields = ['username','email','password1','password2']
        help_text = {key: '' for key in fields} #es una forma de crear un diccionario dado las keys en lista y con valores en vacio (list comprehension)
        
class EditProfileForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    
    page = forms.CharField()
    description = forms.CharField()
    phone_number = forms.CharField()
    job = forms.CharField()
    address = forms.CharField()
    
    avatar = forms.ImageField(required=False)
    