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

""" class Test(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Tests' """