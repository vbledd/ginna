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

# Create your views here.
def index(request):

    #si existe la sesion
    if 'usuario' in request.session:
        #operador
        if request.session['usuario']['perfil'] == 2:
            return redirect('/operador')
        
        #solicitante
        if request.session['usuario']['perfil'] == 3:
            return redirect('/solicitante')
    return render(request, 'login/index.html')


def check_login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')


        #convertir rut a minuscula
        rut = rut.lower()
        
        if Usuario.objects.filter(usuario = user).exists():
            usuario = Usuario.objects.get(usuario = user)

            if check_password(password, usuario.password):

                request.session['usuario'] = {
                    'id': usuario.id,
                    'nombres': usuario.nombres,
                }
                return redirect('/core')

        else:
            request.session['login_message'] = 'Usuario o contraseña incorrectos'
            return redirect('/')
    else:
        request.session['login_message'] = 'Error de metodo'
        return redirect('/')
    
def logout(request):
    del request.session['usuario']
    return redirect('/')

def seleccion(request):

    request.session['login_message'] = ''
    return render(request, 'login/seleccion.html')

def seleccion_data(request):
    fases = Fase.objects.all()
    areas = Area.objects.all()
    tandems = Tandem.objects.all()

    fases_data = []
    areas_data = []
    tandems_data = []

    for fase in fases:
        fases_data.append({
            'id': fase.id,
            'nombre': fase.nombre,
        })

    for area in areas:
        areas_data.append({
            'id': area.id,
            'nombre': area.nombre,
            'fase': area.fase.id,
        })

    for tandem in tandems:
        tandems_data.append({
            'id': tandem.id,
            'nombre': tandem.nombre,
            'area': tandem.area.id,
        })

    context = {
        'fases': fases_data,
        'areas': areas_data,
        'tandems': tandems_data,
    }

    return JsonResponse(context, safe=False)

def guardar_seleccion(request):
    if request.method == 'POST':
        usuario = request.session['usuario']

        if usuario['perfil'] == 2:

            fase = request.POST.get('fase')
            area = request.POST.get('area')

            
            usuario['fase'] = fase
            usuario['area'] = area

            request.session['usuario'] = usuario

            #guardar area y seccion seleccionada en el usuario
            usuario_bd = Usuario.objects.get(id=usuario['id'])
            usuario_bd.fase_seleccionada = Fase.objects.get(id=fase)
            usuario_bd.area_seleccionado = Area.objects.get(id=area)
            usuario_bd.save()

            return redirect('/operador')
                
        if usuario['perfil'] == 3:
            fase = request.POST.get('fase')
            area = request.POST.get('area')
            tandem = request.POST.get('tandem')

            
            usuario['fase'] = fase
            usuario['area'] = area
            usuario['tandem'] = tandem

            request.session['usuario'] = usuario

            #guardar area y seccion seleccionada en el usuario
            usuario_bd = Usuario.objects.get(id=usuario['id'])
            usuario_bd.fase_seleccionada = Fase.objects.get(id=fase)
            usuario_bd.area_seleccionado = Area.objects.get(id=area)
            usuario_bd.tandem_seleccionado = Tandem.objects.get(id=tandem)
            usuario_bd.save()
            return redirect('/solicitante')
            
    else:
        request.session['login_message'] = 'Error de metodo'
        return redirect('/')