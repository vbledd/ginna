from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import *
from django.db import models


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=200)
    usuario = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.nombres

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    def set_password(self, password):
        self.password = make_password(password)

    def check_password(self, password):
        return check_password(password, self.password)

    #save
    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super(Usuario, self).save(*args, **kwargs)

class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)