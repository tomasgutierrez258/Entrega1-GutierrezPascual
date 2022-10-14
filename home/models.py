from django.db import models

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
    # category = models.CharField(max_length = 20)
    # fetured = models.BooleanField()
    text = models.CharField(max_length = 300)
    