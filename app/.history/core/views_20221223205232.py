from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from login.decorador import requiere_login

#import models
from core.models import *



@requiere_login
def index(request):

    registros = Productos.objects.all()
    print("registros", registros)

    return render(request, 'index.html', {'registros': registros})