from django.db import models

# Create your models here.
class Persona2(models.Model):
    nombre = models.CharField(max_length=23)
    edad = models.PositiveIntegerField()
    profesion = models.CharField(max_length=45)




    
