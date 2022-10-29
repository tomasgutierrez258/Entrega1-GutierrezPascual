from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    edad = models.IntegerField()
    mascota = models.CharField(max_length = 30)
    
class Posts(models.Model):
    date = models.DateField(null=True)
    title = models.CharField(max_length = 30)
    brief_description = models.CharField(max_length = 300)
    text = RichTextField(null=True)
    image_post = models.ImageField(upload_to='post_images', null=True, blank=True)
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True) #author
    # user_avatar = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.title