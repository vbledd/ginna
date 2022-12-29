from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.http import HttpResponse


def requiere_login_operador(function):

    def comprobar(request, *callback_args, **callback_kwargs):
        try:
            if request.session['usuario']:
                if request.session['usuario']['perfil'] == 2:

                    if request.session['usuario']['area'] == "":
                        return redirect('/seleccion')
                    return function(request, *callback_args, **callback_kwargs)
                else:
                    raise PermissionDenied
        except Exception as e:
            print(e)
            return redirect('/')

    return comprobar

def requiere_login_solicitante(function):

    def comprobar(request, *callback_args, **callback_kwargs):
        try:
            if request.session['usuario']:
                if request.session['usuario']['perfil'] == 3:
                    if request.session['usuario']['area'] == "":
                        return redirect('/seleccion')
                    return function(request, *callback_args, **callback_kwargs)
                else:
                    raise PermissionDenied
        except Exception as e:
            print(e)
            return redirect('/')

    return comprobar