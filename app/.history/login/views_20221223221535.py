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


        if Usuario.objects.filter(Q(usuario = user) & Q(password = password)).exists():

            usuario = Usuario.objects.get(Q(usuario = user) & Q(password = password))


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
    nombres = request.POST.get('nombres')

    if Usuario.objects.filter(usuario = usuario).exists():
        request.session['login_message'] = 'El usuario ya existe'
        return redirect('/registrar')

    else:
        nuevo_usuario = Usuario()
        nuevo_usuario.usuario = usuario
        nuevo_usuario.nombres = nombres
        nuevo_usuario.password = password
        nuevo_usuario.save()
        request.session['login_message'] = 'Usuario registrado'
        return redirect('/')

def eliminar(request):
    id = request.GET.get('id')

    #buscar id en la session
    reservas = request.session['reservas']

    #eliminar el id
    for reserva in reservas:
        if reserva['id'] == int(id):
            reservas.remove(reserva)
            break
    
    #actualizar la session
    request.session['reservas'] = reservas

    #actualizar el contador
    request.session['contador'] = len(reservas)

    return redirect('/core/reservas')

def terminar_reserva(request):
    #limpiar datos de sesion de reservas
    del request.session['reservas']
    del request.session['contador']

    return redirect('/core/index')
