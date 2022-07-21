from django.db import models

# Create your models here.


class Auto(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.ForeignKey('Marca', on_delete=models.PROTECT)
    nombre = models.CharField(max_length=20)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f'nombre'


class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
