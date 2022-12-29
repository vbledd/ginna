from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.http import HttpResponse


def requiere_login(function):

    def comprobar(request, *callback_args, **callback_kwargs):
        try:
            if request.session['usuario']:
                return function(request, *callback_args, **callback_kwargs)
            else:
                raise PermissionDenied
        except Exception as e:
            print(e)
            return redirect('/')

    return comprobar
