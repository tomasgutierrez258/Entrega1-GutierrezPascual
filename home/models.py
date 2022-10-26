from email.policy import default
from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    edad = models.IntegerField()
    mascota = models.CharField(max_length = 30)
    
class Posts(models.Model):
    author = models.CharField(max_length = 30)
    date = models.DateField(null=True)
    title = models.CharField(max_length = 30)
    brief_description = models.CharField(max_length = 300)
    text = models.CharField(max_length = 300)
    edited = models.BooleanField(default=False)
    image_post = models.ImageField(upload_to='post_images', null=True, blank=True)
    def __str__(self):
        return self.title