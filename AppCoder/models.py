from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni =models.IntegerField()
    user = models.CharField(max_length=16)


class Automotor(models.Model):
    user = models.CharField(max_length=16)
    nchasis = models.CharField(max_length=10)
    nmotor = models.CharField(max_length=10)
    npatente = models.CharField(max_length=7)
    ano = models.IntegerField()

class Registros(models.Model):
    user = models.CharField(max_length=16)
    veiculos = models.IntegerField()

