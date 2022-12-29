from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from login.decorador import requiere_login



@requiere_login
def index(request):
    return render(request, 'index.html')