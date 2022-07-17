from django.db import models
import datetime

# Create your models here.



class Mama(models.Model):
    nombre= models.CharField(max_length=50)
    dni= models.IntegerField()
    fecha_de_nacimiento= models.DateField()


class Papa(models.Model):
    nombre= models.CharField(max_length=50)
    dni= models.IntegerField()
    fecha_de_nacimiento= models.DateField()


class Hermano(models.Model):
    nombre= models.CharField(max_length=50)
    dni= models.IntegerField()
    fecha_de_nacimiento= models.DateField()
    

