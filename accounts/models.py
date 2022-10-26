from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserExtension(models.Model):
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    page = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    