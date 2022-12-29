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

@requiere_login
def historia(request):
    return render(request, 'historia.html')

@requiere_login
def reservar(request):

    id_producto = request.GET.get('id')

    if id_producto:
        print("entro al IF")
        producto = Productos.objects.get(id=id_producto)

        if 'reservas' not in request.session:
            request.session['reservas'] = []
            request.session['contador'] = 0

        guardado = request.session['reservas']
        datos = {
            'id': producto.id,
            'nombre': producto.nombre,
            'precio': producto.precio,
            'imagen': producto.imagen.url,
        }

        guardado.append(datos)
        request.session['reservas'] = guardado

        contador = len(guardado)
        request.session['contador'] = contador

        print("contador" , contador)
        print("guardado", guardado)

        return redirect('/core/index')
    print("ya termino")
    return redirect('/core/index')


@requiere_login
def reservas(request):
    return render(request, 'reservas.html')


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