from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from core.models import *
#import Q
from django.db.models import Q

#import serialize
from django.core import serializers as serialize
#import JsonResponse
from django.http import JsonResponse



def registrar(request):
    return render(request, 'registrar.html')
# Create your views here.
def index(request):

    #si existe la sesion
    if 'usuario' in request.session:
        #operador
        return redirect('/core/index')
    return render(request, 'login/index.html')


def check_login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')


        if Usuario.objects.filter(usuario = user).exists():
            usuario = Usuario.objects.get(usuario = user)

            if check_password(password, usuario.password):

                request.session['usuario'] = {
                    'id': usuario.id,
                    'nombres': usuario.nombres,
                }
                return redirect('/core/index')

        else:
            request.session['login_message'] = 'Usuario o contraseña incorrectos'
            return redirect('/')
    else:
        request.session['login_message'] = 'Error de metodo'
        return redirect('/')
    
def logout(request):
    del request.session['usuario']
    return redirect('/')

def registrar_nuevo(request):
    usuario = request.POST.get('user')
    password = request.POST.get('password')
    
