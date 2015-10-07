from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
    id = models.CharField(max_length=50,primary_key=True)
    nombre = models.CharField(max_length=100,null=True)
    passwd = models.CharField(max_length=128,null=True)
    #use many to many relation ships
    pertenece_conjunto = models.IntegerField(default=0,null=True)
    estatus = models.IntegerField(default=0,null=True)

class User(User):
    pass

class Conjunto(models.Model):
    nombre = models.CharField(max_length=100)
    #use many to many relation ships
    administrador = models.IntegerField(default=0,null=True)
    estatus = models.IntegerField(default=0,null=True  )
    direccion =  models.CharField(max_length=100)
    ciudad =  models.CharField(max_length=25)
    estado =  models.CharField(max_length=25)
    pais =  models.CharField(max_length=15)
    cp =  models.CharField(max_length=10)

class NuevoConjunto(models.Model):
    nombre = models.CharField(max_length=100)
    administrador = models.ForeignKey('Usuario')
    estatus = models.IntegerField(default=0,null=True  )
    direccion =  models.CharField(max_length=100)
    ciudad =  models.CharField(max_length=25)
    estado =  models.CharField(max_length=25)
    pais =  models.CharField(max_length=15)
    cp =  models.CharField(max_length=10)
    conjunto_creado = models.IntegerField(default=0,null=True)

class NuevoUsuario(models.Model):
    id = models.CharField(max_length=50,primary_key=True)
    nombre = models.CharField(max_length=100,null=True)
    pertenece_conjunto = models.ForeignKey('Conjunto')
